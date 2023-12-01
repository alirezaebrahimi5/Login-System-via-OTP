from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
from datetime import datetime, timezone


TOKEN_TYPE_CHOICE = (
    ("PASSWORD_RESET", "PASSWORD_RESET"),
)


class AllUser(BaseUserManager):
    def create_user(self, phone, email, password=None, first_name=None, last_name=None):
        if not email:
            raise ValueError('کاربر باید پست الکترونیکی داشته باشد')
        
        if not phone:
            raise ValueError('کاربر باید شماره تلفن داشته باشد')
        
        if not first_name:
            raise ValueError('کاربر باید شماره نام داشته باشد')
        
        if not last_name:
            raise ValueError('کاربر باید شماره نام خانوادگی داشته باشد')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, phone, email, password, first_name, last_name):
        user = self.create_user(
            email=email,
            phone=phone,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active  = False
        user.is_superuser = False        
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, password, first_name, last_name):
        user = self.create_user(
            email=email,
            phone=phone,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active  = True
        user.is_superuser = True        
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email      = models.EmailField(unique=True)
    password   = models.CharField(max_length=255, null=True)
    firstname  = models.CharField(max_length=255)
    lastname   = models.CharField(max_length=255)
    image      = models.FileField(upload_to="users/", blank=True, null=True)
    phone      = models.CharField(max_length=30, unique=True, blank=True, null=True)
    is_locked  = models.BooleanField(default=False)
    is_staff   = models.BooleanField(default=False)
    is_active  = models.BooleanField(default=False)
    is_admin   = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    verified   = models.BooleanField(default=False)
    
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    
    objects = AllUser()

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.phone

    def save_last_login(self) -> None:
        self.last_login = datetime.now()
        self.save()
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class AuditableModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class PendingUser(AuditableModel):
    phone =  models.CharField(max_length=20)
    verification_code = models.CharField(max_length=8, blank=True, null=True)
    password = models.CharField(max_length=255, null=True)


    def __str__(self):
        return f"{str(self.phone)} {self.verification_code}"
    
    def is_valid(self) -> bool:
        """10 mins OTP validation"""
        lifespan_in_seconds = float(settings.OTP_EXPIRE_TIME * 60)
        now = datetime.now(timezone.utc)
        time_diff = now - self.created_at
        time_diff = time_diff.total_seconds()
        if time_diff >= lifespan_in_seconds:
            return False
        return True


class Token(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    token = models.CharField(max_length=8)
    token_type = models.CharField(max_length=100, choices=TOKEN_TYPE_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.user)} {self.token}"

    def is_valid(self) -> bool:
        lifespan_in_seconds = float(settings.TOKEN_LIFESPAN * 60 )
        now = datetime.now(timezone.utc)
        time_diff = now - self.created_at
        time_diff = time_diff.total_seconds()
        if time_diff >= lifespan_in_seconds:
            return False
        return True

    def reset_user_password(self, password: str) -> None:
        self.user.set_password(password)
        self.user.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    email = models.EmailField(verbose_name='پست الکترونیکی')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    first_name  = models.CharField(max_length=30, null=True, blank=True, verbose_name='نام')
    last_name   = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام خانوادگی')
    
    def __str__(self) -> str:
        return f"{self.user} {self.email}"
