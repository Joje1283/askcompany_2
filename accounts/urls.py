from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
