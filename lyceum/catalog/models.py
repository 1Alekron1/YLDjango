from django.db import models
from core.models import IdBaseModel, PublishedIdBaseModel, SlugBaseModel
from django.core import validators
from .validators import validate_words_brilliants
from django.contrib.auth import get_user_model


User = get_user_model()


class Tag(PublishedIdBaseModel, SlugBaseModel):

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.slug[:15]


class Category(PublishedIdBaseModel, SlugBaseModel):
    weight = models.IntegerField(default=100, validators=[
                                 validators.MinValueValidator(1), validators.MaxValueValidator(32766)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.slug[:15]


class Item(PublishedIdBaseModel):
    name = models.CharField('Название', max_length=150,
                            help_text='Макс 150 символов')

    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag)

    text = models.TextField('Описание', validators=[validate_words_brilliants],
                            help_text='Минимум два слова. Обязательно содержится слово превосходно или роскошно')
    
    ratings = models.ManyToManyField(
        User, verbose_name='Товар',  through='rating.Rating', through_fields=('item', 'user'))

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name[:15]
