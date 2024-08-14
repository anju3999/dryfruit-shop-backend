from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'date_of_birth')
    search_fields = ('user__username', 'phone_number')
