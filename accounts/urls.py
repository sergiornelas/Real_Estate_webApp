#when you want to create a path, you have to import the module 'path' each time:
from django.urls import path

#import all views using .
from . import views

urlpatterns = [
    #first parameter: empty path means home directory like /
    #second parameter: method we want to connect in the view file
    #third parameter: name to easily access this path
    
    path('login', views.login, name='login'),
    path('register', views.register, name='register'), #views.listing refers to the listing method.
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]