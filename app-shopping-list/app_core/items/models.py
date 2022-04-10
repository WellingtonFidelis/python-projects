from django.db import models

# Create your models here.
class Item(models.Model):
  description = models.CharField(max_length=200, blank=False, null=True)
  cost = models.DecimalField(default=0, max_digits=8, decimal_places=2, blank=False, null=True)
  date_created = models.DateField(auto_now_add=True)
  date_purchase = models.DateField(auto_now=True)