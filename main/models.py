from django.db import models

from common.models import BaseModel


# Create your models here.
class Catalogs(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Products(BaseModel):
    catalog = models.ForeignKey(Catalogs, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return self.name