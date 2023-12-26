from django.urls import path

from . import views

urlpatterns = [
    path('registration', views.UserView.register),
    path('auth/<str:login>', views.UserView.login),

    path('friends/find/<str:login>', views.FindFriend.as_view()),
    path('chats/<str:login>', views.CreateChat.as_view()),
    path('location', views.GetLocations.as_view()),
    path('location/<str:login>', views.GetLocations.as_view())
]

