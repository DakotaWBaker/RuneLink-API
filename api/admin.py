from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):    
    model = CustomUser
    list_display = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(GroupFinder)