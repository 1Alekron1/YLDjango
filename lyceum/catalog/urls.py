from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.item_list),
    path('1', views.item_detail),
    path('2', views.item_detail),
]
