from django.urls import path

from users import views

urlpatterns = [
    path("users/", views.user_list),
    path("users/<int:number>/", views.user_detail),
    path("signup/", views.signup),
    path("profile/", views.profile),
]
