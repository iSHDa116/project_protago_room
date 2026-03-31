from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accont/', include('accounts.urls')),
    path('',include('games.urls')),
    path('',include('reviews.urls')),

]
