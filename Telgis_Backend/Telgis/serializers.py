from rest_framework import serializers

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    """
       Сериализатор для модели Users.

       Преобразует объекты Users в формат JSON и наоборот.
       """

    class Meta:
        model = Users
        fields = ['login', 'password_hash', 'avatar_url']


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['password_hash']


class AuthenticationSuccessSerializer(serializers.Serializer):
    """
        Сериализатор для успешного успеха "OK".

    """
    status = serializers.CharField(
        default="login"
    )

class BadRequestErrorSerializer(serializers.Serializer):
    """
    Сериализатор для ошибки "Bad Request".

    Используется для возврата сообщения об ошибке с HTTP-статусом 400.
    """

    status = serializers.CharField(
        default="Error.",
        help_text="Сообщение об ошибке",
    )


class NotFoundErrorSerializer(serializers.Serializer):
    """
    Сериализатор для ошибки "Not Found".

    Используется для возврата сообщения об ошибке с HTTP-статусом 404.
    """

    status = serializers.CharField(
        default="Not found.",
        help_text="Сообщение об ошибке",
    )


class InternalServerErrorSerializer(serializers.Serializer):
    """
    Сериализатор для ошибки "Internal Server Error".

    Используется для возврата сообщения об ошибке с HTTP-статусом 500.
    """

    detail = serializers.CharField(
        default="Internal server error.",
        help_text="Сообщение об ошибке",
    )
