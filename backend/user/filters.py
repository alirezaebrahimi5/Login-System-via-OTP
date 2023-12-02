import django_filters

from .models import User 
from .enums import ROLE_CHOICE


class UserFilter(django_filters.FilterSet):   
    class Meta:
        model = User
        fields = ['verified']
