from django.contrib import admin
from .models import FoodDelivery
class FoodDeliveryAdmin(admin.ModelAdmin):
    list_display = ('OrderID','UserID','OrderDate','ItemName','OrderQty','UnitPrice','TotalAmount','DeliveryAddress')
    list_filter = ('OrderDate','ItemName','UnitPrice','TotalAmount')
admin.site.register(FoodDelivery,FoodDeliveryAdmin)
