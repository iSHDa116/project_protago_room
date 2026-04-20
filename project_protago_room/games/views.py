import zipfile
import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, TemplateView, DetailView, DeleteView)
from reviews.models import Like
from . import forms
from . import models

#ユーザーの権限
class AdminOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff
    
# Create your views here.
class HomeView(TemplateView):
    template_name = 'games/index.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        gold_games = []

        for dept in ['J', 'A', 'S']:
            game = models.Game.objects.filter(
                concours='Gold',
                department=dept,
                is_published=True
            ).first()

            if game:
                gold_games.append(game)
        
        context['gold'] = models.Game.objects.filter(concours='Gold')
        context['silver'] = models.Game.objects.filter(concours='Silver')
        context['bronze'] = models.Game.objects.filter(concours='Bronze')
        return context
        # context['popular'] = models.Game.objects.annotate()

class PlayView(DetailView):
    template_name = 'games/game_play.html'
    model = models.Game
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        game = self.object
        user = self.request.user

        #いいね済か否か
        liked = False
        if(user.is_authenticated):
            liked = Like.objects.filter(user=user, game=game).exists()

        like_count = Like.objects.filter(game=game).count()        

        context['liked'] = liked
        context['like_count'] = like_count

        return context

class GameListView(ListView):
    model = models.Game
    template_name = 'games/game_list.html'
    #テンプレートに、名前をつけてデータを渡している
    context_object_name = 'games'

class GameUploadView(AdminOnlyMixin,CreateView):
    template_name = 'games/game_upload.html'
    model = models.Game
    form_class = forms.GameForm
    success_url = reverse_lazy('games_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        game = self.object
        #ファイルの場所を取得
        if (game.game_file):
            zip_path = game.game_file.path
            
            extract_path = os.path.join(settings.MEDIA_ROOT, 'games', str(game.id))
            
            os.makedirs(extract_path, exist_ok=True)
            
            #zipファイルを開く
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                #全て解凍
                zip_ref.extractall(extract_path)
            
        return response
    
class GameDeleteView(AdminOnlyMixin,DeleteView):
    template_name = "games/game_delete.html"
    model = models.Game
    success_url = reverse_lazy('games_list')

