# Generated by Django 3.2 on 2022-03-22 16:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating', '0004_auto_20220320_1824'),
        ('catalog', '0006_auto_20220320_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ratings',
            field=models.ManyToManyField(through='rating.Rating', to=settings.AUTH_USER_MODEL, verbose_name='Товар'),
        ),
    ]
