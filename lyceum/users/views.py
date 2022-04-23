from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Prefetch
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


from .models import Profile
from catalog.models import Item, Tag
from rating.models import Rating
from .forms import ChangeProfileForm, ChangeUserForm


def user_list(request):
    users = User.objects.all().select_related(
        "profile",
    )
    context = {"users": users}
    return render(request, "users/user_list.html", context=context)


def user_detail(request, number):
    user = User.objects.get(pk=number)
    items = Item.objects.favourite_items(user)
    context = {"user": user, "items": items, "path": "user_detail"}
    return render(request, "users/user_detail.html", context=context)


def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегестрировались")
            return redirect("homepage")
        messages.error(request, "Некорректные данные")
    form = NewUserForm()
    return render(
        request=request,
        template_name="users/signup.html",
        context={"register_form": form},
    )


def profile(request):
    items = Item.objects.favourite_items(request.user)
    if request.method == "POST":
        user_form = ChangeUserForm(request.POST, instance=request.user)
        profile_form = ChangeProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
    else:
        user_form = ChangeUserForm(instance=request.user)
        profile_form = ChangeProfileForm(instance=request.user.profile)
    context = {"items": items, "user_form": user_form, "profile_form": profile_form}
    return render(request, "users/profile.html", context=context)
