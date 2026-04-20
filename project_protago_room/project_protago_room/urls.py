from django.contrib import admin
# from django.contrib.auth.urls import 
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('',include('games.urls')),
    path('',include('reviews.urls')),

]
