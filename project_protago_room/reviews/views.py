from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Like
from games.models import Game
# Create your views here.
@login_required
def toggle_like(request, game_id):
    user = request.user
    game = get_object_or_404(Game, id=game_id)
    
    # like　いいねの状態、　#いいねが既に押されているか否か
    like, created = Like.objects.get_or_create(user=user, game=game)
    
    #もし "いいいね"が押されていないなら
    if(created):
        liked=True
    else:
        like.delete()
        liked = False
    
    #いいねの計算
    like_count = Like.objects.filter(game=game).count()
    
    return JsonResponse({"liked":liked, "count":like_count})