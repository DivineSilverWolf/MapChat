from django.urls import path

from Telgis.views import UserView, FindFriendView, ChatView

urlpatterns = [
    # path('/<int:user_id>', UserView.user_id_details),
    # path('', UserView.user_details),
    # path('/login', UserView.login),
    # path('/find-friend', FindFriendView.as_view())

    path('registration', UserView.register),
    path('auth/<str:login>', UserView.login),
    path('friends/find/<str:login>', FindFriendView.as_view()),
    path('chats/<str:login>', ChatView.as_view())
]

