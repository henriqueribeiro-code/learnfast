
from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

urlpatterns = [
    path('entrar/', auth_view.LoginView.as_view(), name='login'),
    path('registrar/', register , name='register'),
]
