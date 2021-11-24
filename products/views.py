from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class ProductView(View):
    def get(self,request):
        products=Product.objects.all()
        return render(request,'products/product.html',{'products':products})