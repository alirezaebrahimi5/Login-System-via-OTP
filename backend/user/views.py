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


class AuthViewsets(viewsets.GenericViewSet):
    """Auth viewsets"""
    serializer_class = EmailSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        permission_classes = self.permission_classes
        if self.action in ["initiate_password_reset", "create_password", "verify_account"]:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(
        methods=["POST"],
        detail=False,
        serializer_class=InitiatePasswordResetSerializer,
        url_path="initiate-password-reset",
    )
    def initiate_password_reset(self, request, pk=None):
        """Send temporary OTP to user phone to be used for password reset"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True,
                         "message": "Temporary password sent to your mobile!"}, status=200)

    @action(methods=['POST'], detail=False, serializer_class=CreatePasswordFromResetOTPSerializer, url_path='create-password')
    def create_password(self, request, pk=None):
        """Create a new password given the reset OTP sent to user phone number"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token: Token = Token.objects.filter(
            token=request.data['otp'],  token_type=TokenEnum.PASSWORD_RESET).first()
        if not token or not token.is_valid():
            return Response({'success': False, 'errors': 'Invalid password reset otp'}, status=400)
        token.reset_user_password(request.data['new_password'])
        token.delete()
        return Response({'success': True, 'message': 'Password successfully reset'}, status=status.HTTP_200_OK)

    @extend_schema(
        responses={
            200: inline_serializer(
                name='AccountVerificationStatus',
                fields={
                    "success": serializers.BooleanField(default=True),
                    "message": serializers.CharField(default="Acount Verification Successful")
                }
            ),
        },
    )
    @action(
        methods=["POST"],
        detail=False,
        serializer_class=AccountVerificationSerializer,
        url_path="verify-account",
    )
    def verify_account(self, request, pk=None):
        """Activate a user acount using the verification(OTP) sent to the user phone"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "message": "Acount Verification Successful"}, status=200)
