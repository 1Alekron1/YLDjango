from django.urls import path

from users import views

urlpatterns = [
    path("users/", views.user_list, name="all_users"),
    path("users/<int:number>/", views.user_detail),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("signin", views.signin, name="signin"),
    path("logout", views.logout_request, name="logout"),
]
