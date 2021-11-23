from django.db import models
from user.models import CustomUser
from cart.models import Cart
# Create your models here.

class Order(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address=models.CharField(max_length=255,default='')
    order_description=models.TextField(default='')
    is_completed=models.BooleanField(default=False)