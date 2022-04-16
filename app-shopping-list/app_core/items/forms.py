from django import forms
from items.models import Item

class ItemModelForm(forms.Form):
  class Meta:
    model = Item
    fields = [
      "description",
      "cost",
    ]
    
  ''' def clean_description(self, *args, **kwargs):
    description = self.cleaned_data.get("description")
  
    if len(description) < 1:
      raise forms.ValidationError("The description must be has some description")
    else:
      return description '''
    
  def clean_cost(self, *args, **kwargs):
    cost = self.cleaned_data.get("cost")
    if cost <= 0:
      raise forms.ValidationError("The price must be bigger than 0")
    else:
      return cost
      
    
  description = forms.CharField(
    label="Description",
    initial="",
    widget=forms.TextInput(
      attrs={
        "type": "text",
        "class": "form-control",
        "id": "inputDescription",
        "name": "inputDescription",
        "placeholder": "Enter a description"
      }
    )
  )
  cost = forms.DecimalField(
    label="Value (R$)",
    initial=0,
    widget=forms.TextInput(
      attrs={
        "type": "number",
        "class": "form-control",
        "id": "inputCost",
        "name": "inputCost",
        "min": 0,
        "placeholder": "Enter the price"
      }
    )
  )