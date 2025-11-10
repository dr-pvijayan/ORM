# Ex02 Django ORM Web Application
## Date: 10.11.2025

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![WhatsApp Image 2025-09-13 at 11 18 52_5d24c06f](https://github.com/user-attachments/assets/988601d0-de11-4499-b64b-fd1a6531b1d3)


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
## Manage.py
```python
from django.db import models

# Create your models here.
class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    price = models.IntegerField()
    year = models.DateField()
```

## Admin.py

```python
from django.contrib import admin
from . models import Car

admin.site.register(Car)
class carAdmin(admin.ModelAdmin):
    list_display = ('car_id','brand','model','price','year')

```


## OUTPUT
<img width="1920" height="1080" alt="Screenshot 2025-09-22 085715" src="https://github.com/user-attachments/assets/6fdf2489-7d11-4865-90c2-4e2806ee9540" />



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
