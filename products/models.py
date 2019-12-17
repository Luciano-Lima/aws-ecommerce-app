from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='') #defaut means its the first product
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=6)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name