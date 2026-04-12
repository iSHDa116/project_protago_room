from django.contrib import admin
# from django.contrib.auth.urls import 
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accont/', include('django.contrib.auth.urls')),
    path('',include('games.urls')),
    path('',include('reviews.urls')),

]
