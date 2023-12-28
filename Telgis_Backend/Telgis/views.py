import json

from django.db.models import Q
import rest_framework.request
from django.contrib.auth.hashers import make_password, check_password

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .decorators import check_auth_schema, check_reg_schema, check_get_schema
from .models import Users, Friends, Chats, ChatMembers, Locations
from .serializers import UserSerializer, LocationSerializer


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
            return JsonResponse({'message': 'Login can only contain letters and numbers'}, status=400)

        if len(password) < 6 or len(password) > 20:
            return JsonResponse({'message': 'Password must be between 6 and 20 characters'}, status=400)
        if not any(char.isdigit() for char in password):
            return JsonResponse({'message': 'Password must contain at least one digit'}, status=400)
        if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?`~' for char in password):
            return JsonResponse({'message': 'Password must contain at least one special character'}, status=400)

        avatar_url = ""
        status = "offline"

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


class FindFriend(APIView):
    def post(self, request, login):
        friend_login = request.data.get('login')

        similar_users = Users.objects.filter(login__icontains=friend_login).exclude(login=login)

        if similar_users.exists():
            potential_friends = [user for user in similar_users if
                                 not Friends.objects.filter(login_friend_one=user.login,
                                                            login_friend_two=login).exists()]

            if potential_friends:
                serializer = UserSerializer(potential_friends, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("No potential friends found", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("No users found", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, login):

        users = Users.objects.all().exclude(login=login)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateChat(APIView):
    def post(self, request, login):
        data = request.data

        friends = data.get('friends', [])
        chat_name = data.get('chat_name')

        chat = Chats.objects.create(chat_name=chat_name, chat_type="")

        user = get_object_or_404(Users, login=login)
        ChatMembers.objects.create(chat_id=chat, login=user)

        for friend in friends:
            user = get_object_or_404(Users, login=friend)
            ChatMembers.objects.create(chat_id=chat, login=user)

        return Response("success", status=status.HTTP_200_OK)


class GetLocations(APIView):
    def post(self, request):
        data = request.data
        print(data, "ITS COORDINATES")
        serializer = LocationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = request.data
        print(data, "ITS GETLOCATIONS")
        friends_locations = self.get_friends_locations(data['login'])
        return Response(friends_locations, status=status.HTTP_200_OK)

    def get_friends_locations(self, login):
        friends = Friends.objects.filter(Q(login_friend_one=login) | Q(login_friend_two=login))
        friend_logins = [
            friend.login_friend_one.login if friend.login_friend_one.login != login else friend.login_friend_two.login
            for friend in friends]
        friend_locations = Locations.objects.filter(login__in=friend_logins)
        serialized_locations = LocationSerializer(friend_locations, many=True).data
        return serialized_locations


# class AddFriend(APIView):
#
#     def post(self, request, login):
#         pass
#
#
# class FriendsList(APIView):
#
#     def post(self, request):
#         pass
#
#
# class FriendsConfirm(APIView):
#
#     def get(self, request):
#         pass
#
#
# class FindFriends(APIView):
#
#     def post(self, request, login):
#         pass


@check_auth_schema
class Authentication(APIView):

    @csrf_exempt
    def post(self, request, login):
        try:
            password = request.data.get('password')

            # # Проверка, что получены и username, и password
            # if not username or not password:
            #     return JsonResponse({'status': 'error', 'message': 'Username and password are required'}, status=400)

            user = get_object_or_404(Users, login=login)
            print(user.login, user.password)

            if check_password(password, user.password):

                return JsonResponse({'status': 'login'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@check_reg_schema
class Registration(APIView):

    @csrf_exempt
    def post(self, request):  #: rest_framework.request.Request
        try:
            data = request.data
            print(data)
            login = data['login']
            password = data['password']
            avatar_url = "none"
            status = "online"
            if Users.objects.filter(login=login).exists():
                return JsonResponse({'status': 'error', 'message': 'User already exists'}, status=400)

            users = Users(login=login, password=make_password(password), avatar_url=avatar_url, status=status)
            users.save()
            print("OK")
            return JsonResponse({"status": "success"})

        except Exception as e:
            print(f"Error in Registration view: {e}")
            return JsonResponse({'status': 'error', 'message': 'Internal Server Error'}, status=500)

    # def patch(self, request):
    #     try:
    #         data = request.data[0]
    #         login = data['login']
    #
    #         if not Users.objects.filter(login=login).exists():
    #             return JsonResponse({'status': 'error', 'message': 'User not found'})
    #
    #         password = data['password_hash']
    #         avatar_url = data['avatar_url']
    #         status = data['status']
    #
    #         Users.objects.filter(login=login).update(password_hash=password, avatar_url=avatar_url,
    #                                                  status=status)
    #         return JsonResponse({'status': 'success'})
    #     except KeyError as e:
    #         return JsonResponse({'status': 'error', 'message': f'Missing key: {str(e)}'})
    #
    #     except Exception as e:
    #         return JsonResponse({'status': 'error', 'message': str(e)})


@check_get_schema
class UserIdDetails(APIView):
    @csrf_exempt
    def get(self, request, login):
        user = get_object_or_404(Users, login=login)
        data = {
            'login': user.login,
            'password': user.password,
            'avatar_url': user.avatar_url,
            'status': user.status
        }
        return JsonResponse(data)

    @csrf_exempt
    def delete(self, requset, login):
        user = get_object_or_404(Users, login=login)
        user.delete()
        return JsonResponse({'status': 'success'})
