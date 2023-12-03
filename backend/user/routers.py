from rest_framework import routers

from .views import *


router = routers.SimpleRouter()

router.register("", AuthViewsets,  basename="auth")
router.register("change-password", PasswordChangeView, basename="password-change")
