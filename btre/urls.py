from django.contrib import admin
from django.urls import path 
from django.urls import include #if you want to use 'include' keyword

#new added
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #
    path('', include('pages.urls')), #linking the urls.py of the pages app. #'' = homepage
    path('listings/', include('listings.urls')),
    #
    path('admin/', admin.site.urls),
    
    #new added
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
