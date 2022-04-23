from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()


class ClassChangeForm(forms.BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
            return user


class ChangeUserForm(forms.ModelForm, ClassChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ChangeProfileForm(forms.ModelForm, ClassChangeForm):
    class Meta:
        model = Profile
        fields = ("birthday",)
        widgets = {"birthday": forms.DateInput(attrs={"type": "date"})}
