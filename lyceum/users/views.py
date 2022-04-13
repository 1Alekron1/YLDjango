from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def user_list(request):
    context = {}
    return render(request, "users/user_list.html", context=context)


def user_detail(request, number):
    context = {
        "number": number
    }  # функция уже была с параметром, переделывать было слишком затратно, решили оставить с контекстом
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


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                messages.error(request, "Неправильное имя пользователя или пароль.")
        else:
            messages.error(request, "Неправильное имя пользователя или пароль.")
    form = AuthenticationForm()
    return render(
        request=request, template_name="users/signin.html", context={"login_form": form}
    )


def logout_request(request):
    logout(request)
    return redirect("homepage")


def profile(request):
    context = {}
    return render(request, "users/profile.html", context=context)
