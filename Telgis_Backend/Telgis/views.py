import json

import rest_framework.request
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from .decorators import *
from .models import Users


class AddFriend(APIView):

    def post(self, request, login):
        pass


class FriendsList(APIView):

    def post(self, request):
        pass


class FriendsConfirm(APIView):

    def get(self, request):
        pass


class FindFriends(APIView):

    def post(self, request, login):
        pass


@check_auth_schema
class Authentication(APIView):

    @csrf_exempt
    def post(self, request, login):
        try:
            password = request.data.get('password_hash')

            # # Проверка, что получены и username, и password
            # if not username or not password:
            #     return JsonResponse({'status': 'error', 'message': 'Username and password are required'}, status=400)

            user = get_object_or_404(Users, login=login)
            if check_password(password, user.password_hash):

                return JsonResponse({'status': 'login'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=401)
            return JsonResponse({'status': 'login'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@check_reg_schema
class Registration(APIView):

    @csrf_exempt
    def post(self, request):        #: rest_framework.request.Request
        try:
            data = request.data
            print(data)
            login = data['login']
            password = make_password(data['password'])
            avatar_url = "none"
            status = "online"
            if Users.objects.filter(login=login).exists():
                return JsonResponse({'status': 'error', 'message': 'User already exists'}, status=400)

            users = Users(login=login, password_hash=make_password(password), avatar_url=avatar_url, status=status)
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
            'password_hash': user.password_hash,
            'avatar_url': user.avatar_url,
            'status': user.status
        }
        return JsonResponse(data)

    @csrf_exempt
    def delete(self, requset, login):
        user = get_object_or_404(Users, login=login)
        user.delete()
        return JsonResponse({'status': 'success'})
