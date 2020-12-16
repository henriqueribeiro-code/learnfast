
from django.urls import path
from django.contrib.auth import views as loginViews

urlpatterns = [
    path('entrar/', loginViews.LoginView,{ 'template_name': 'accounts/index.html' }, name='login'),
]
