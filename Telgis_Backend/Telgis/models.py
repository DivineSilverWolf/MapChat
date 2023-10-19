from django.db import models


class Users(models.Model):
    user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password_hash = models.CharField(max_length=128)
    avatar_url = models.CharField(max_length=120)
    status = models.CharField(max_length=255)


class Friends(models.Model):
    friendship = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Users', on_delete=models.DO_NOTHING, related_name='id_пользователя')
    friend_id = models.ForeignKey('Users', on_delete=models.DO_NOTHING, related_name='id_друга')
    status = models.CharField(max_length=255)


class Chats(models.Model):
    chat = models.AutoField(primary_key=True)
    chat_name = models.CharField(max_length=30)
    chat_type = models.CharField(max_length=30)


class Messages(models.Model):
    message = models.AutoField(primary_key=True)
    chat_id = models.ForeignKey('Chats', on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey('Users', on_delete=models.DO_NOTHING)
    message_text = models.TextField()
    timestamp = models.DateTimeField()


class Locations(models.Model):
    location = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField()


class ChatMembers(models.Model):
    chat_member = models.AutoField(primary_key=True)
    chat_id = models.ForeignKey('Chats', on_delete=models.CASCADE)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
