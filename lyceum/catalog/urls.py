from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.item_list, name="all_items"),
    path("<int:pk>/", views.item_detail, name="item_detail"),
]
