from django.urls import path , include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import *


router = routers.SimpleRouter()

router.register("", AuthViewsets,  basename="auth")
router.register("change-password", PasswordChangeView, basename="password-change")


urlpatterns = [
    path("login/", CustomObtainTokenPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("token/verify/", TokenVerifyView.as_view(), name="verify-token"),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path("", include(router.urls)),
]
