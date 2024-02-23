from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',Index.as_view(), name='index' ),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),

]
