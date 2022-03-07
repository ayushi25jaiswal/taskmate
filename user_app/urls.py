from user_app import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),


]