from drf_spectacular.utils import (
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)

from .serializers import *

check_auth_schema = extend_schema_view(
    post=extend_schema(
        request=AuthSerializer(),
        summary="Метод для аутентификации пользователей",
        description="Этот метод позволяет пройти аутентификацию\n\n"
                    "Пример POST-запроса:\n\n"
                    "{\n\n"
                    '    "password_hash": "password_hash"\n\n'
                    "}",
        responses={
            200: OpenApiResponse(
                response=AuthenticationSuccessSerializer,
                description="Пользователь успешно авторизован.",
            ),
            404: OpenApiResponse(
                response=BadRequestErrorSerializer,
                description="Error: Пользователь не найден",
            ),
        }
    )

)
check_reg_schema = extend_schema_view(
    post=extend_schema(
        request=RegisterSerializer(many=True),
        summary="Метод для регистрации пользователей",
        description="Этот метод позволяет добавить пользователя\n\n"
                    "Пример POST-запроса:\n\n"
                    "{\n\n"
                    '    "login": "example",\n\n'
                    '    "password": "password_hash"\n\n'
                    '    "avatar_url": "url",\n\n'
                    "}",
        responses={
            200: OpenApiResponse(
                response=AuthenticationSuccessSerializer,
                description="Пользователь успешно зарегистрирован.",
            ),
            400: OpenApiResponse(
                response=BadRequestErrorSerializer,
                description="Error: Пользователь с таким логином уже существует",
            ),

        },
    ),
    # patch=extend_schema(
    #     request=UsersSerializer(many=True),
    #     summary="Метод для изменения объектов Users",
    #     description="Этот метод позволяет изменить текущего пользователя\n\n"
    #                 "Пример POST-запроса:\n\n"
    #                 "{\n\n"
    #                 '    "login": "example",'
    #                 '    "password": "password_hash"\n\n'
    #                 '    "avatar_url": "url",'
    #                 '    "status": "status_name"'
    #                 "}",
    #     responses={
    #         200: OpenApiResponse(
    #             description="Пользователь успешно изменен.",
    #         ),
    #         400: OpenApiResponse(
    #             response=BadRequestErrorSerializer,
    #             description="Error: Bad Request",
    #         ),
    #         404: OpenApiResponse(
    #             response=NotFoundErrorSerializer,
    #             description="Error: Not Found",
    #         ),
    #         500: OpenApiResponse(
    #             response=InternalServerErrorSerializer,
    #             description="Error: Internal server error",
    #         ),
    #     },
    # ),
)

check_get_schema = extend_schema_view(
    get=extend_schema(
        request=RegisterSerializer(many=True),
        summary="Метод для просмотра объектов Users",
        description="Этот метод позволяет просмотреть данные пользователя\n\n",

        responses={
            200: OpenApiResponse(
                description="Пользователь найден.",
            ),
            400: OpenApiResponse(
                response=BadRequestErrorSerializer,
                description="Error: Bad Request",
            ),
            404: OpenApiResponse(
                response=NotFoundErrorSerializer,
                description="Error: Not Found",
            ),
            500: OpenApiResponse(
                response=InternalServerErrorSerializer,
                description="Error: Internal server error",
            ),
        }, ),

    delete=extend_schema(
        request=RegisterSerializer(many=True),
        summary="Метод для удаления объектов Users",
        description="Этот метод позволяет удалить пользователя\n\n",

        responses={
            200: OpenApiResponse(
                description="Пользователь успешно удален.",
            ),
            400: OpenApiResponse(
                response=BadRequestErrorSerializer,
                description="Error: Bad Request",
            ),
            404: OpenApiResponse(
                response=NotFoundErrorSerializer,
                description="Error: Not Found",
            ),
            500: OpenApiResponse(
                response=InternalServerErrorSerializer,
                description="Error: Internal server error",
            ),
        },
    )
)
