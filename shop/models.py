from django.db import models
from django.db.models.deletion import CASCADE

from django.contrib.auth.models import User 

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images', null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = (('completed', 'completed'), ('pending', 'pending'))

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f"Order Id {self.pk}"