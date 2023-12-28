from django.urls import path

from . import views

urlpatterns = [
  #  path('registration', views.UserView.register),
  # path('auth/<str:login>', views.UserView.login),

    path('friends/<str:login>', views.FindFriend.as_view()),
    path('chats/<str:login>', views.CreateChat.as_view()),
    path('location', views.GetLocations.as_view()),
    # path('location/<str:login>', views.GetLocations.as_view()),
    path('registration', views.Registration.as_view(), name='register'),
    path('auth/<str:login>', views.Authentication.as_view(), name='login'),
    path('<str:login>/', views.UserIdDetails.as_view()),
    # path('friends/find/<str:login>'),
    # path('friends/add/<str:login>'),
    # path('friends/list/'),
    # path('friends/confirm/'),

]

