from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Rating(models.Model):
    choices = (
        ("0", "Смешанные чувства"),
        ("1", "Ненависть"),
        ("2", "Неприязнь"),
        ("3", "Нейтрально"),
        ("4", "Обожание"),
        ("5", "Любовь"),
    )
    star = models.CharField("Оценка", max_length=1, choices=choices, default=0)
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE, default=""
    )
    item = models.ForeignKey(
        to="catalog.Item", verbose_name="Товар", on_delete=models.CASCADE, default=""
    )

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        constraints = [
            UniqueConstraint(
                fields=[
                    "item",
                    "user",
                ],
                name="unique_rating",
            )
        ]

    def __str__(self):
        return str(self.user)
