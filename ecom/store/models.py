from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True,db_index=True)
    #slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/images/')

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(default=0)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    placed_at = models.DateTimeField(datetime.datetime.now)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    order_id = models.UUIDField(unique=True)



    def __str__(self):
        return f'{self.order_id} {self.customer.first_name} {self.customer.last_name}'
    



