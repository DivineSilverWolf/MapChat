from django.urls import path

from Telgis import views

urlpatterns = [
    path('/<int:user_id>', views.user_id_details),
    path('', views.user_details),
    path('/login', views.login)
]

