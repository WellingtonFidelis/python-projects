from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from items.models import Item
from items.forms import ItemModelForm

# Create your views here.
class ItemsView():
  def home(request):
    items = Item.objects.all()
    
    total = 0
    
    for item in items:
      if item.is_purchased:
        total += item.cost
    
    context = {
      "items": items,
      "total": total
    }
    
    template = "../templates/base.html"
    
    return render(request=request, template_name=template, context=context)
  
  def list(request):
    items = Item.objects.all()
    template = "items/item_list.html"
    context = {
      "items": items
    }
    return render(request=request, template_name=template, context=context)
  
  def create(request):
    initial_data = {
      "description": "",
      "cost": 0
    }    
    form = ItemModelForm(request.POST or None, initial=initial_data)    
    if form.is_valid():
      Item.objects.create(**form.cleaned_data)
      form = ItemModelForm()
      return redirect(reverse("home"))    
    template = "items/item_create.html"    
    context = {
      "form": form
    }    
    return render(request=request, template_name=template, context=context)
  
  def edit(request, pk):
    item = Item.objects.get(pk=pk)
    item.is_purchased = True
    item.save()
    template = "items/item_create.html"
    context = {
      "item": item
    }
    return redirect(reverse("home")) 