from django.db import models
from django.core import validators


class IdBaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, validators=[
                             validators.MinValueValidator(0)], help_text='Больше 0')

    class Meta:
        abstract = True


class PublishedIdBaseModel(IdBaseModel):
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True


class SlugBaseModel(models.Model):
    slug = models.CharField('Название', max_length=200, unique=True,
                            validators=[validators.RegexValidator])

    class Meta:
        abstract = True
