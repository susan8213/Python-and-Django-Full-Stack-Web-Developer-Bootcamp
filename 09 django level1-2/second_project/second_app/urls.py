from django.urls import path
from second_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help', views.help, name='help'),
    path('users', views.users, name='users'),
]