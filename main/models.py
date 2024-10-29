from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=50,default=None)
    price=models.IntegerField(default=None)
    def __str__(self):
        return self.title

class Log(models.Model):
    Log_types=[
        ('create','Create'),('update','Update'),('delete','Delete')
    ]
    type=models.CharField(max_length=10,choices=Log_types)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
    message=models.TextField(max_length=100,default=None)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.title