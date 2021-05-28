from django.db import models

# Create your models here.

class Product(models.Model):
    categories=[
        ('tech products','tech products'),
        ('clothes','clothes'),
    ]
    title=models.CharField(max_length=120)
    description = models.TextField(null=True)
    price =  models.DecimalField(decimal_places=2,max_digits=10)
    category = models.CharField(choices=categories,max_length=50,null=True)


    def __str__(self):
        return self.title
