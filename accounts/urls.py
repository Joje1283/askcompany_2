from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),  # /accounts/login/ => settings.LOGIN_URL
    path('logout/', views.logout, name='logout'),
    path('password_change/', views.password_change, name='password_change'),
    path('signup/', views.signup, name='signup'),
    path('edit/', views.profile_edit, name='profile_edit'),
]
