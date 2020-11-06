from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),  # /accounts/login/ => settings.LOGIN_URL
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
