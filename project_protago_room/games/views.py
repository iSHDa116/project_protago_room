from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, )
from .models import Game

# Create your views here.
def index_view(request):
    return render(request, 'games/index.html')

class GameListView(ListView):
    template_name = 'games/game_list.html'
    model = Game

class GameUploadView(CreateView):
    template_name = 'games/game_upload.html'
    model = Game
    fields = ['title', 'description', 'game_link', 'thumbnail_url']
    success_url = reverse_lazy('index')