from django.urls import path

from homepage import views
from lyceum import settings

urlpatterns = [
    path(
        "",
        views.home,
        name="homepage",
    )
]
