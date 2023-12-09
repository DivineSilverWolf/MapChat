from django.urls import path

from . import views

urlpatterns = [
    path('registration/', views.Registration.as_view(), name='register'),
    path('auth/<str:login>', views.Authentication.as_view(), name='login'),
    path('<str:login>/', views.UserIdDetails.as_view()),

]

