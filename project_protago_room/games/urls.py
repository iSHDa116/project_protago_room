from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('',views.HomeView.as_view(),name=('game_index')),
    path('game/list/', views.GameListView.as_view(), name=('games_list')),
    path('game/upload/', views.GameUploadView.as_view(), name=('game_upload')),
    path('game/<int:pk>/play', views.PlayView.as_view(),name=('game_play')),
    path('game/delete/<int:pk>/', views.GameDeleteView.as_view(), name=('game_delete')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
