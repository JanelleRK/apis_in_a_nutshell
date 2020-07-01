from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    website = models.URLField(max_length=300, null=True)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=20)


    def __str__(self):
        return self.style



class ShoeColor(models.Model):
    RED = 'Red'
    ORANGE = 'Orange'
    YELLOW = 'Yellow'
    GREEN = 'Green'
    BLUE = 'Blue'
    INDIGO = 'Indigo'
    VIOLET = 'Violet'
    WHITE = 'White'
    BLACK = 'Black'
    SHOE_COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
    ]
    color_name = models.CharField(
        max_length=6,
        choices=SHOE_COLOR_CHOICES,
        default=BLACK,
    )

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=30)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=30)

    def __str__(self):
        return self.shoe_type

#Probably not true but I heard that Joe was raised by hyenas and that is why he has such an awesome and contagious laugh.