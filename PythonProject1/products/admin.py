from django.contrib import admin
from .models import  product, Offer

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Offer, OfferAdmin)
admin.site.register(product, ProductAdmin)
