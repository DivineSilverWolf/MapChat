from django.db import models


class Users(models.Model):
    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    login = models.CharField(primary_key=True, max_length=20, default='none')
    password_hash = models.CharField(max_length=128)
    avatar_url = models.CharField(max_length=120)
    status = models.CharField(max_length=255)


class Friends(models.Model):
    class Meta:
        verbose_name = 'Друзья'
        verbose_name_plural = 'Друзья'

    friendship = models.AutoField(primary_key=True)
    login_friend_one = models.ForeignKey('Users', on_delete=models.DO_NOTHING, related_name='id_друга1', default='none')
    login_friend_two = models.ForeignKey('Users', on_delete=models.DO_NOTHING, related_name='id_друга2', default='none')
    status = models.ForeignKey('FriendsStatus', on_delete=models.DO_NOTHING, related_name='статус')


class FriendsStatus(models.Model):
    class Meta:
        verbose_name = 'Статусы'
        verbose_name_plural = 'Статусы'

    status = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=255)


class Chats(models.Model):
    class Meta:
        verbose_name = 'Чаты'
        verbose_name_plural = 'Чаты'

    chat = models.AutoField(primary_key=True)
    chat_name = models.CharField(max_length=30)
    chat_type = models.CharField(max_length=30)


class ChatMembers(models.Model):
    class Meta:
        verbose_name = 'Участники чата'
        verbose_name_plural = 'Участники чата'

    chat_member = models.AutoField(primary_key=True)
    chat_id = models.ForeignKey('Chats', on_delete=models.DO_NOTHING, default='none')
    login = models.ForeignKey('Users', on_delete=models.DO_NOTHING, default='none')


class Messages(models.Model):
    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'

    message = models.AutoField(primary_key=True)
    chat_id = models.ForeignKey('Chats', on_delete=models.DO_NOTHING)
    login = models.ForeignKey('Users', on_delete=models.DO_NOTHING, default='none')
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Locations(models.Model):
    class Meta:
        verbose_name = 'Местоположения'
        verbose_name_plural = 'Местоположения'

    location = models.AutoField(primary_key=True)
    login = models.ForeignKey('Users', on_delete=models.CASCADE, default='none')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
