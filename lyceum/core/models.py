from django.core import validators
from django.db import models


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField("Опубликовано", default=True)

    class Meta:
        abstract = True


class SlugBaseModel(models.Model):
    slug = models.CharField(
        "Название", max_length=200, unique=True, validators=[validators.RegexValidator]
    )

    class Meta:
        abstract = True
