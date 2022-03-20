from django.db import models
from Core.models import IdBaseModel
from django.core import validators
from django.contrib.auth import get_user_model
from catalog.models import Item
from django.db.models import UniqueConstraint

User = get_user_model()


class Rating(IdBaseModel):
    star = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(
        5)], help_text='от 1 до 5. Соответствие: 1- "Ненависть", 2 - "Неприязнь", 3 - "Нейтрально", 4 -"Обожание", 5 - "Любовь".  Возможно нулевое значение.')

    user = models.ManyToManyField(User)
    item = models.ManyToManyField(Item)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        # d = {1: "Ненависть", 2: "Неприязнь", 3: "Нейтрально",
        #      4: "Обожание", 5: "Любовь", 0: "Смешанные чувства"}

        return str(self.star)
