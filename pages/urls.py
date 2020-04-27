#when you want to create a path, you have to import the module 'path' each time:
from django.urls import path

#import all views using .
from . import views

urlpatterns = [
    #first parameter: empty path means home directory like /
    #second parameter: method we want to connect in the view file
    #third parameter: name to easily access this path
    path('', views.index, name='index'),
    path('sobre', views.zoo, name='about'),
]