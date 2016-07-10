from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    company=models.CharField(max_length=100)


    def __str__(self):
        return self.company

class Product(models.Model):
    product=models.CharField(max_length=200)
    company=models.ForeignKey(Company)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=10)
    stock=models.IntegerField(default=0)

    def __str__(self):
        return self.product

class Review(models.Model):
    product=models.ForeignKey(Product)
    user=models.ForeignKey(User)
    publish_data=models.DateField(default=timezone.now)
    text=models.TextField()

    def __str__(self):
        return self.text

class Cart(models.Model):
    user=models.ForeignKey(User)
    active=models.BooleanField(default=True)
    order_date=models.DateField(null=True)
    payment_type=models.CharField(max_length=100,null=True)
    payment_id= models.CharField(max_length=100,null=True)

    def add_to_cart(self,product_id):
            product=Product.object.get(pk=product_id)
            try:
                preexisting_order=ProductOder.objects.get(product=product,cart=self)
                preexisting_order.quantity+=1
                preexisting_order.save()
            except ProductOrder.DoesNoExist:
                new_order=ProductOrder.objects.create(
                    product=name,
                    cart=self,
                    quantity=1
                )
                new_order.save()
    def remove_from_cart(self,product_id):
            product=Product.objects.get(pk=product_id)
            try:
                preexisting_order= ProductOrder.objects.get(product=product,cart=self)
                if preexisting_order.quantity >1 :
                    preexisting_order.quantity-=1
                    preexisting_order.save()
                else:
                    preexisting_order.delete()
            except ProductOrder.DoesNoExist:
                pass




class ProductOrder(models.Model):
    book=models.ForeignKey(Product)
    cart=models.ForeignKey(Cart)
    quantity=models.IntegerField()
