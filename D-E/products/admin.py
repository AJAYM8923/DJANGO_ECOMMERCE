from django.contrib import admin
from products.models import Product, Cart, user_address, Order, OrderItem, contact_details, Collection

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(user_address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(contact_details)
admin.site.register(Collection)