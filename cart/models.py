from django.db import models
from products.models import Variation
from user.models import CustomUser
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    item=models.ForeignKey(Variation,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)