from django.urls import path
from .views import SignupView, SignupDoneView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('signup/done/', SignupDoneView.as_view(), name='signup_done'),
]
