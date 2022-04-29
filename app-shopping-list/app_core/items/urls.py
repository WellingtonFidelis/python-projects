from django.urls import path

from . import views

urlpatterns = [
    path("", views.list, name="home"),
    path("item-list/", views.list, name="item-list"),
    path("item-create/", views.create, name="item-create"),
    path("item-update/<int:pk>", views.edit, name="item-edit"),
]

