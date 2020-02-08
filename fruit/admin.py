from django.contrib import admin
from .models import Fruit,Offer

class FruitAdmin(admin.ModelAdmin):
  list_display =("name","price","stock")

class OfferAdmin(admin.ModelAdmin):
  list_display = ("code","discount")
admin.site.register(Fruit,FruitAdmin)
admin.site.register(Offer,OfferAdmin)
