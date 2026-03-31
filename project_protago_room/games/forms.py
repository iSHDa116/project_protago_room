from django import forms
from .models import Game
from django.contrib.admin.widgets import AdminDateWidget

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'creater','school', 'description', 'game_type', 'game_link', 'game_file', 'thumbnail_url', ]
        
        labels = {
            'title':'作品名',
            'creater':'作者',
            'school':'所属校舎',
            'description':'説明',
            'game_type':'Unity or Scratch',
            'game_link':'スクラッチURL',
            'game_file':'Unityフォルダ',
            'thumbnail_url':'サムネ画像',
        }