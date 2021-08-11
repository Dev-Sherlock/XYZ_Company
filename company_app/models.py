from django.db import models

class Product(models.Model):
    categories=[
        ('tech products','tech products'),
        ('clothes','clothes'),
    ]
    title=models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/% Y/% m/% d/')
    description = models.TextField(null=True)
    price =  models.DecimalField(decimal_places=2,max_digits=10)
    category = models.CharField(choices=categories,max_length=50,null=True)
    avaliable = models.BooleanField(default=True,blank=True)

    def __str__(self):
        return self.title
