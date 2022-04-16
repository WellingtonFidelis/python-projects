from django.urls import path, include

from items.views import ItemsView

urlpatterns = [
  path("", ItemsView.home, name="home"),
  path("item-list/", ItemsView.list, name="item-list"),
  path("item-create/", ItemsView.create, name="item-create"),
  path("item-update/<int:pk>", ItemsView.edit, name="item-edit"),
]