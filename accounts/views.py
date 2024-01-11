from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# from . models import UserProfile
# from store.models import Product
from .models import User_details


# Create your views here.

def Home(request):
    return render(request,'register.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    form = RegistrationForm()
    return render(request, 'register.html', {'form' : form})

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('Register')
    return render(request, 'login.html')


def profile(request, usernam=None):
    if usernam:
        profile = User.objects.get(username = usernam)
        return render(request, 'profile.html', {'profile':profile})
    return redirect('Login')

def user_logout(request):
    logout(request)
    return redirect('Login')

def dashboard(request):
    user = User_details.objects.order_by('-accurate')
    return render(request, 'dashboard.html', {'user':user})