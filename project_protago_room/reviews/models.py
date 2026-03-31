from django.db import models
from django.contrib.auth.models import User
from games.models import Game

class Like(models.Model):
    # intで数えると、ずれが発生するため、keyでカウントする
    #誰が
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #どのゲームに
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        #重複防止
        unique_together = ('user', 'game')