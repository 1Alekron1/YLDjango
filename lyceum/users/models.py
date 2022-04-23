from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    email = models.EmailField("Почта", unique=True)
    username = models.CharField(("Имя пользователя"), max_length=50, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = [
            "email",
        ]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField("День рождения", blank=True, null=True)

    class Meta:
        verbose_name = "Дополнительное поле"
        verbose_name_plural = "Дополнительные поля"

    def __str__(self):
        return f"День рождения пользователя: {self.user.username}"


@receiver(post_save, sender=User)
def save_aand_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class UserManager(BaseUserManager):
    def _create_user(self, email, password, username, **extra_fields):
        if not email:
            raise ValueError("Укажите вашу почту")
        if not password:
            raise ValueError("Укажите пароль")
        if not username:
            raise ValueError("Укажите пользователя")
        email = self.normalize

        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("У администраторов должно быть is_superuser=True.")
        return self._create_user(username, email, password, **extra_fields)
