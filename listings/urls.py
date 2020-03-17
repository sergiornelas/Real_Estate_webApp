#when you want to create a path, you have to import the module 'path' each time:
from django.urls import path

#import all views using .
from . import views

urlpatterns = [
    #first parameter: empty path means home directory like /
    #second parameter: method we want to connect in the view file
    #third parameter: name to easily access this path
    
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'), #views.listing refers to the listing method.
        #pk=listing_id de views.py
        #<int:listing_id> es el 2 de: http://localhost:8000/listings/2
    path('search', views.search, name='search'),
]