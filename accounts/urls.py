from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.Home, name='hom'),
    path('register/',views.register, name='Register'),
    path('login/',views.user_login, name='Login'),
    path('logout/',views.user_logout, name='Logout'),
    path('profile/',views.profile, name='Profile'),
    path('profile/<str:usernam>/',views.profile, name='Profiles'),
    path('dashboard/', views.dashboard, name='dashboard'),
]