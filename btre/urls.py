from django.contrib import admin
from django.urls import path 
from django.urls import include #if you want to use 'include' keyword

urlpatterns = [
    #
    path('', include('pages.urls')), #linking the urls.py of the pages app. #'' = homepage
    path('listings/', include('listings.urls')),
    #
    path('admin/', admin.site.urls),   
]