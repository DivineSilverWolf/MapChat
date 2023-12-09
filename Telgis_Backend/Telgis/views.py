import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Users, Friends, Chats, ChatMembers
from .serializers import UserSerializer


class UserView:
    @csrf_exempt
    def register(request):
        if request.method != 'POST':
            return HttpResponse('Invalid Request')

        data = json.loads(request.body)

        if data.get('login') is None or data.get('password') is None:
            return JsonResponse({'message': 'Login and password cannot be empty'}, status=400)

        login = data['login']
        password = data['password']

        if Users.objects.filter(login=login).exists():
            return JsonResponse({'message': 'User already exists'}, status=400)

        if len(login) < 6 or len(login) > 20:
            return JsonResponse({'message': 'Login must be between 6 and 20 characters'}, status=400)
        if not login.isalnum():
            return JsonResponse({'message': 'Login can only contain letters and numbers'}, status=400 )

        if len(password) < 6 or len(password) > 20:
            return JsonResponse({'message': 'Password must be between 6 and 20 characters'}, status=400)
        if not any(char.isdigit() for char in password):
            return JsonResponse({'message': 'Password must contain at least one digit'}, status=400)
        if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?`~' for char in password):
            return JsonResponse({'message': 'Password must contain at least one special character'}, status=400)

        avatar_url = ""
        status = "offline"

        #users = Users(username=username, email=email, password_hash=password, avatar_url=avatar_url, status=status)
        users = Users(login=login, password_hash=password, avatar_url=avatar_url, status=status)
        users.save()

        return JsonResponse({'login': login})

    def delete_user(self, user):
        user.delete()
        return JsonResponse({'status': 'success'})

    def edit_user(self, request):
        data = json.loads(request.body)
        user = data['user']

        if not Users.objects.filter(user=user).exists():
            return JsonResponse({'message': 'User not found'})

        username = data['username']
        password = data['pass']
        email = data['email']
        avatar_url = data['avatar_url']
        status = data['status']

        users = Users(user=user, username=username, email=email, password_hash=password, avatar_url=avatar_url,
                      status=status)
        users.save()
        return JsonResponse({'status': 'success'})

    def get_user(self, user):
        data = {
            'user': user.user,
            'username': user.username,
            'email': user.email,
            'password_hash': user.password_hash,
            'avatar_url': user.avatar_url,
            'status': user.status
        }
        return JsonResponse(data)

    @csrf_exempt
    def user_details(request):
        view = UserView()
        if request.method == 'POST':
            return view.add_user(request)
        elif request.method == 'PATCH':
            return view.edit_user(request)
        else:
            return HttpResponse('Invalid Request')

    @csrf_exempt
    def user_id_details(request, user_id):
        user = get_object_or_404(Users, user=user_id)
        view = UserView()
        if request.method == 'GET':
            return view.get_user(user)
        elif request.method == 'DELETE':
            return view.delete_user(user)
        else:
            return HttpResponse('Invalid Request')

    @csrf_exempt
    def login(request, login):
        if request.method != 'POST':
            return HttpResponse('Invalid Request')

        data = json.loads(request.body)

        if data.get('password') is None:
            return JsonResponse({'message': 'Password cannot be empty'}, status=400)

        password = data['password']

        if not Users.objects.filter(login=login).exists():
            return JsonResponse({'message': 'User not found'}, status=404)

        user = get_object_or_404(Users, login=login)

        if (user.password_hash == password):
            user.status = 'online'
            user.save()

            return JsonResponse({'login': login})
        else:
            return JsonResponse({'message': 'Incorrect password'}, status=400)


class FindFriendView(APIView):
    def post(self, request, login):
        friend_login = request.data.get('login')

        similar_users = Users.objects.filter(login__icontains=friend_login).exclude(login=login)

        if similar_users.exists():
            potential_friends = [user for user in similar_users if
                                 not Friends.objects.filter(login_friend_one=user.login, login_friend_two=login).exists()]

            if potential_friends:
                serializer = UserSerializer(potential_friends, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("No potential friends found", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("No users found", status=status.HTTP_404_NOT_FOUND)


class ChatView(APIView):
    def post(self, request, login):
        friends = request.data.get('friends', [])

        chat = Chats.objects.create(chat_name="", chat_type="")

        user = Users.objects.get(login=login)
        ChatMembers.objects.create(chat_id=chat, login=user.login)

        for friend in friends:
            user = Users.objects.get(login=friend)
            ChatMembers.objects.create(chat_id=chat, login=user.login)

        return Response(status=status.HTTP_200_OK)