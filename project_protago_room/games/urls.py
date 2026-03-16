from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index_view,name=('index')),
    path('game/list/', views.GameListView.as_view(), name=('list')),
    path('game/upload/', views.GameUploadView.as_view(), name=('upload')),
    path('game/play', views.play_view,name=('play')),
]
