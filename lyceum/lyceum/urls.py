from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("about/", include("about.urls")),
    path("auth/", include("users.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += staticfiles_urlpatterns()
