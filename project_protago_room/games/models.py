from django.db import models

class Game(models.Model):
    
    
    SCHOOL_CHOICES = [('eifuku','永福町'),('goutokuji','豪徳寺'),('odakyuSagamihara','小田急相模原'),]
    GAMETYPE_CHOICES = [('scratch','スクラッチ') , ('unity','Unity'),]
    CONCOURS = [('Gold','金賞'),('Silver','銀賞'),('Bronze','銅賞')]
    
    title = models.CharField(max_length=50, verbose_name='作品名')
    creater = models.CharField(max_length=25, verbose_name='作者', blank=True, null=True)
    school = models.CharField(max_length=25, verbose_name='所属校舎',choices=SCHOOL_CHOICES , blank=True, null=True)

    description = models.TextField(verbose_name='説明')

    #ゲームの種類(スクラッチ or Unity)を選ぶ
    game_type = models.CharField(verbose_name='Unity or Scratch', max_length=10, choices=GAMETYPE_CHOICES)
    # スクラッチ(url形式)
    game_link = models.URLField(verbose_name='作品リンク',blank=True, null=True) 
    #unityプロジェクト(ファイル形式)
    game_file = models.FileField(upload_to='games/', blank=True, null=True)

    thumbnail_url = models.ImageField(
            upload_to='thumbnails/',
            verbose_name='サムネイル',
            blank=True,
            null=True)
    is_published = models.BooleanField(default=True) #公開・非公開・審査の判定
    play_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    #コンクール受賞か否か
    concours = models.TextField(choices=CONCOURS, blank=True, null=True)    
    def __str__(self):
        return self.title

