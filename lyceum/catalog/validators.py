from django.forms import ValidationError


def validate_brilliants(value):
    if "превосходно" not in value and "роскошно" not in value:
        raise ValidationError(f'Используйте любое из "превосходно" или "роскошно"')


def validate_words(value):
    if len(value.split()) < 2:
        raise ValidationError(f"Используйте больше {quantity}-х слов")
