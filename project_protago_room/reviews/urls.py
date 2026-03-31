from django.urls import path
from . import views

urlpatterns = [
    path('like/<int:game_id>/',views.toggle_like,name=('review_like')),
]
