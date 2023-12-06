from django.urls import path

from Telgis.views import UserView, FindFriendView

urlpatterns = [
    path('/<int:user_id>', UserView.user_id_details),
    path('', UserView.user_details),
    path('/login', UserView.login),
    path('/find-friend', FindFriendView.as_view())
]

