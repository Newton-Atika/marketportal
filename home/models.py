from django.db import models
import uuid
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(blank=False)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = CloudinaryField('image',default='None')
    sav = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    picked = models.BooleanField(default=False) 

    def __str__(self):
        return f'Shopping List {self.unique_id}'
