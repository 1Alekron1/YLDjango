# Generated by Django 3.2 on 2022-03-23 17:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(choices=[('0', 'Смешанные чувства'), ('1', 'Ненависть'), ('2', 'Неприязнь'), ('3', 'Нейтрально'), ('4', 'Обожание'), ('5', 'Любовь')], default=0, max_length=1, verbose_name='Оценка')),
                ('item', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='catalog.item', verbose_name='Товар')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('item', 'user'), name='unique_rating'),
        ),
    ]
