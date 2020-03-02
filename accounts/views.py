from django.shortcuts import render, redirect

#message alerts
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        #message alerts
        messages.error(request, 'Testing error message')
        return redirect('register')
        #
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        #Login User
        return
    else:
        return render(request, 'accounts/login.html')

#función que redirige a una pagina, no la renderea
def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')