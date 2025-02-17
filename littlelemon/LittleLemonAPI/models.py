from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 4, decimal_places=2, default = 0)
    inventory = models.PositiveIntegerField(validators=[MaxValueValidator(10000)])

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'