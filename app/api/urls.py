from django.urls import path
from . import views

urlpatterns = [
    path('callback', views.bot_callback, name='bot_callback'),
]