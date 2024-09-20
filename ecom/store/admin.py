from django.contrib import admin

from . models import Category, Product, Customer, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","name","price"]

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","first_name","last_name","email"]



admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order)


# Register your models here.
