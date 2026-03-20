from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, )
from . import models

# Create your views here.
def index_view(request):
    return render(request, 'games/index.html')

def play_view(request, pk):
    game = get_object_or_404(models.Game, pk=pk)
    context = {'game_link': game.game_link}
    return render(request, 'games/game_play.html',context)

class GameListView(ListView):
    model = models.Game
    template_name = 'games/game_list.html'
    #テンプレートに、名前をつけてデータを渡している
    context_object_name = 'games'

class GameUploadView(CreateView):
    template_name = 'games/game_upload.html'
    model = models.Game
    fields = ['title', 'description', 'game_link', 'thumbnail_url']
    success_url = reverse_lazy('games_list')   
    