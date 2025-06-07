from django.db import models

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Product ka naam
    sku = models.CharField(max_length=50, unique=True)  # Stock Keeping Unit (unique id)
    category = models.CharField(max_length=50)  # Product category
    quantity = models.PositiveIntegerField()  # Kitne items stock mein hain
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per item
    
    def __str__(self):
        return self.name
