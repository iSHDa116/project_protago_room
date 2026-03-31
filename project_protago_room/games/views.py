import zipfile
import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, TemplateView, DetailView )
from reviews.models import Like
from . import forms
from . import models

# Create your views here.
class HomeView(TemplateView):
    template_name = 'games/index.html'

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

class GameUploadView(CreateView):
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