from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse
from items.models import Item
from items.forms import ItemModelForm


# Create your views here.
def home(self, request):
    items = Item.objects.all()

    template = loader.get_template("../templates/base.html")

    context = {
        "items": items,
    }

    return HttpResponse(template.render(context, request))


def list(request):
    items = Item.objects.all()
    template = loader.get_template("items/item_list.html")
    context = {
        "items": items,
        "total_value_items_purchased": total_value_items_purchased(items),
        "total_value_items_to_buy": total_value_items_to_buy(items),
    }
    return HttpResponse(template.render(context, request))


def create(request):
    initial_data = {
        "description": "",
        "cost": 0
    }
    form = ItemModelForm(request.POST or None, initial=initial_data)
    if request.method == "POST":
        if form.is_valid():
            Item.objects.create(**form.cleaned_data)
            form = ItemModelForm()
            return redirect(reverse("home"))

    template = loader.get_template("items/item_create.html")

    context = {
        "form": form
    }

    return HttpResponse(template.render(context, request))


def edit(request, pk):
    item = Item.objects.get(pk=pk)
    item.is_purchased = True
    item.save()
    return redirect(reverse("home"))


def total_value_items_purchased(items):
    total = 0
    for item in items:
        if item.is_purchased:
            total += item.cost

    return total


def total_value_items_to_buy(items):
    total = 0
    for item in items:
        if not item.is_purchased:
            total += item.cost

    return total
