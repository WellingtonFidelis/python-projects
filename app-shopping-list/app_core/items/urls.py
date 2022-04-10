from django.urls import path

from items.views import ItemsView

urlpatterns = [
  path("", ItemsView.list, name="items"),
]