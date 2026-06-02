from django.db import models

class FoodDelivery(models.Model):
    OrderID = models.IntegerField(primary_key=True)
    UserID = models.IntegerField()
    OrderDate = models.IntegerField()
    ItemName = models.CharField()
    OrderQty = models.IntegerField()
    UnitPrice=models.IntegerField()
    TotalAmount=models.IntegerField()
    DeliveryAddress=models.CharField()
    