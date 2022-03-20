from django.forms import ValidationError


def validate_words_brilliants(value):
    if len(value.split()) < 2 and ('превосходно' not in value and 'роскошно' not in value):
        raise ValidationError(
            f'Используйте больше 2-х слов, а также любое из "превосходно" или "роскошно"')
