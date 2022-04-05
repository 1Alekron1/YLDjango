from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from core.models import PublishedBaseModel, SlugBaseModel

from .validators import validate_brilliants, validate_words

User = get_user_model()


class Tag(PublishedBaseModel, SlugBaseModel):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.slug[:15]


class Category(PublishedBaseModel, SlugBaseModel):
    weight = models.IntegerField(
        default=100,
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(32766),
        ],
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.slug[:15]


class Item(PublishedBaseModel):
    name = models.CharField("Название", max_length=150, help_text="Макс 150 символов")

    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.CASCADE
    )

    tags = models.ManyToManyField(Tag)
    text = models.TextField(
        "Описание",
        validators=[validate_words, validate_brilliants],
        help_text="Минимум два слова. Обязательно содержится слово превосходно или роскошно",
    )

    ratings = models.ManyToManyField(
        User,
        verbose_name="Товар",
        through="rating.Rating",
        through_fields=("item", "user"),
    )

    def __str__(self):
        return self.name[:10]

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name[:15]
