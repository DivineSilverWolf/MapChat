from django.contrib import admin

# Register your models here.
from .models import *


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'avatar_url')


admin.site.register(FriendsStatus)

admin.site.register(Users)
admin.site.register(Messages)
admin.site.register(Locations)
admin.site.register(Friends)
admin.site.register(Chats)
admin.site.register(ChatMembers)

admin.site.site_header = "Админ-панель Telgis"
admin.site.site_title = "Админ"