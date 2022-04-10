from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from items.models import Item

# Create your views here.
class ViewItems():
  def list(request):
    items = Item.objects.all()
    template = loader.get_template("items/index.html")
    context = {
      "items": items
    }
    #output = ", ".join([items["description"].all() for item in items])
    return HttpResponse(template.render(context,request))