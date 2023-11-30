from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

from .models import User


class Admin(UserAdmin):
    list_display = ('phone', 'email', 'fullName', 'is_active', 'pk', 'joined_at')
    filter_horizontal = ()
    list_filter = (('joined_at', JDateFieldListFilter), 'is_active')
    fieldsets = ()
    search_fields = ('email', 'phone', 'fullName')
    list_display_links = ('phone', 'email')
    # This line below added because 'ordering' attribute need a dependency
    ordering = ('email', 'joined_at')


class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'email', 'pk']
    search_fields = ('phone', 'user')
    sortable_by = ('pk', 'user')


admin.site.register(User, Admin)
