from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50, verbose_name='作品名')
    description = models.TextField(verbose_name='説明')
    game_link = models.URLField(verbose_name='作品リンク') #このフィールドにゲームのリンクを春ことでアップロードが可能になる
    thumbnail_url = models.URLField(verbose_name='サムネイル')
    is_published = models.BooleanField(default=True) #公開・非公開・審査の判定
    play_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

