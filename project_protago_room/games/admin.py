from django.contrib import admin
from .models import Game

class AdminGame(admin.ModelAdmin):
    list_display = ('title','game_type',)

admin.site.register(Game, AdminGame)