from django.http import HttpResponse


def user_list(request):
    return HttpResponse("Список пользователей")


def user_detail(request, number):
    return HttpResponse(f"Информация о пользователе {number}")


def signup(request):
    return HttpResponse("Регистрация")


def profile(request):
    return HttpResponse("Мой профиль")
