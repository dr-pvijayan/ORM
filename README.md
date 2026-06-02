# Ex01 Django ORM Web Application
## Date: 19-05-2026

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
ADMIN.PY

from django.contrib import admin
from .models import FoodDelivery
class FoodDeliveryAdmin(admin.ModelAdmin):
    list_display = ('OrderID','UserID','OrderDate','ItemName','OrderQty','UnitPrice','TotalAmount','DeliveryAddress')
    list_filter = ('OrderDate','ItemName','UnitPrice','TotalAmount')
admin.site.register(FoodDelivery,FoodDeliveryAdmin)

MODEL.PY
from django.db import models
```
```
class FoodDelivery(models.Model):
    OrderID = models.IntegerField(primary_key=True)
    UserID = models.IntegerField()
    OrderDate = models.IntegerField()
    ItemName = models.CharField()
    OrderQty = models.IntegerField()
    UnitPrice=models.IntegerField()
    TotalAmount=models.IntegerField()
    DeliveryAddress=models.CharField()
```

    


## OUTPUT
![alt text](<Screenshot 2026-05-19 112624.png>)

![alt text](<Screenshot 2026-05-19 112334.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
