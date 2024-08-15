from django.contrib import admin
from django.contrib.auth import get_user_model

from clients.models.clients import Client

# Register your models here.

@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')

