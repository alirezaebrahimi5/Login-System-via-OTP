from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import filters, serializers, status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, Token, Profile
from .serializers import (AuthTokenSerializer,OnboardUserSerializer,
                          CreatePasswordFromResetOTPSerializer,
                          CustomObtainTokenPairSerializer, EmailSerializer,
                          ListUserSerializer, PasswordChangeSerializer,
                          AccountVerificationSerializer,InitiatePasswordResetSerializer,
                          UpdateUserSerializer)
from .filters import UserFilter
from .enums import TokenEnum


class CustomObtainTokenPairView(TokenObtainPairView):
    """Authentice with phone number and password"""
    serializer_class = CustomObtainTokenPairSerializer
