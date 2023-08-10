from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect("/login")

def loginUser(request):
    if request.method == 'POST':
        #checking useres correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')    

def logoutUser(request):
    logout(request)
    return redirect('/login')