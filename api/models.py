from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    website = models.URLField(max_length= 300, null=True)


class ShoeType(models.Model):
    style = models.CharField(max_length=40)


class ShoeColor(models.Model):
    color_name = models.CharField(max_length=30)


class Shoe(models.Model):
    size = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=30)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=30)