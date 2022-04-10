from django.urls import path

from items import views

urlpatterns = [
  path("", views.ViewItems.list, name="items"),
]