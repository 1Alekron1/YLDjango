from django.shortcuts import render


def user_list(request):
    context = {}
    return render(request, "users/user_list.html", context=context)


def user_detail(request, number):
    context = {
        "number": number
    }  # функция уже была с параметром, переделывать было слишком затратно, решили оставить с контекстом
    return render(request, "users/user_detail.html", context=context)


def signup(request):
    context = {}
    return render(request, "users/signup.html", context=context)


def profile(request):
    context = {}
    return render(request, "users/profile.html", context=context)
