import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Users

def add_user(request):
    data = json.loads(request.body)

    username = data['login']
    email = data['email']
    password = data['pass']

    if Users.objects.filter(username=username).exists():
        return JsonResponse({'message': 'User already exists'})

    if len(username) < 6 or len(username) > 20:
        return JsonResponse({'message': 'Username must be between 6 and 20 characters'})
    if not username.isalnum():
        return JsonResponse({'message': 'Username can only contain letters and numbers'})

    if len(password) < 6 or len(password) > 20:
        return JsonResponse({'message': 'Password must be between 6 and 20 characters'})
    if not any(char.isdigit() for char in password):
        return JsonResponse({'message': 'Password must contain at least one digit'})
    if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?`~' for char in password):
        return JsonResponse({'message': 'Password must contain at least one special character'})

    avatar_url = data['avatar_url']
    status = data['status']

    users = Users(username=username, email=email, password_hash=password, avatar_url=avatar_url, status=status)
    users.save()

    return JsonResponse({'login': username})


def delete_user(user):
    user.delete()
    return JsonResponse({'status': 'success'})


def edit_user(request):
    data = json.loads(request.body)
    user = data['user']

    if not Users.objects.filter(user=user).exists():
        return JsonResponse({'message': 'User not found'})

    username = data['username']
    email = data['email']
    avatar_url = data['avatar_url']
    status = data['status']

    users = Users(user=user, username=username, email=email, password_hash=password, avatar_url=avatar_url,
                  status=status)
    users.save()
    return JsonResponse({'status': 'success'})


def get_user(user):
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
    if request.method == 'POST':
        return add_user(request)
    elif request.method == 'PATCH':
        return edit_user(request)
    else:
        return HttpResponse('Invalid Request')


@csrf_exempt
def user_id_details(request, user_id):
    user = get_object_or_404(Users, user=user_id)
    if request.method == 'GET':
        return get_user(user)
    elif request.method == 'DELETE':
        return delete_user(user)
    else:
        return HttpResponse('Invalid Request')

@csrf_exempt
def login(request):
    if request.method != 'POST':
        return HttpResponse('Invalid Request')

    data = json.loads(request.body)

    if data.get('login') is None or data.get('pass') is None:
        return JsonResponse({'message': 'Username and password cannot be empty'})

    username = data['login']
    password = data['pass']

    if not Users.objects.filter(username=username).exists():
        return JsonResponse({'message': 'User not found'}, status=404)

    user = get_object_or_404(Users, username=username)

    if(user.password_hash == password):
        user.status = 'online'
        user.save()

        return JsonResponse({'login': username})
    else:
        return JsonResponse({'message': 'Incorrect password'})




