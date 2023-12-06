from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Token, Profile


class Admin(UserAdmin):
    list_display = ('phone', 'email', 'fullName', 'is_locked', 'is_active', 'pk', 'created_at')
    filter_horizontal = ()
    list_filter = ('created_at', 'is_active')
    fieldsets = ()
    search_fields = ('email', 'phone', 'fullName')
    list_display_links = ('phone', 'email')
    # This line below added because 'ordering' attribute need a dependency
    ordering = ('email', 'created_at')


class TokenAdmin(admin.ModelAdmin):
    list_display = ["user", "token"]
    search_fields = ['user']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'pk', 'fullName']
    search_fields = ('phone', 'user')
    sortable_by = ('pk', 'user')


admin.site.register(User, Admin)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(Token, TokenAdmin)
