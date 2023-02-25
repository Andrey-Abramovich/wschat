from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    list_filter = ['username']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['name']


class MesageAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'date')


admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MesageAdmin)
