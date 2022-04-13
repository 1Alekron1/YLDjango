from django import forms
from rating.models import Rating


class RatingSelect(forms.Form):
    CHOICES = Rating.choices
    rating = forms.ChoiceField(
        widget=forms.RadioSelect, choices=CHOICES, label="Оценка"
    )
