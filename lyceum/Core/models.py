from django.db import models
from django.core import validators


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
