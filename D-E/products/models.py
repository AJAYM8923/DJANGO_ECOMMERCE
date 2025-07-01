from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='uploads/', null=True, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True, blank=True)




class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to Django's User model
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to Product model
    quantity = models.PositiveIntegerField(default=1)  # Default quantity is 1



class user_address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    alt_phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=100)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)  # New field for delivery date
    status = models.CharField(max_length=20, default='Pending')  # Example: Pending, Completed, Canceled

    def save(self, *args, **kwargs):
        # Set delivery date automatically to 10 days after order date
        if not self.delivery_date:
            self.delivery_date = self.date + timedelta(days=10)
        super(Order, self).save(*args, **kwargs)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class contact_details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()