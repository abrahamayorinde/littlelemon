from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    No_of_guests = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],default = 0)
    BookingDate = models.DateTimeField()

    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 4, decimal_places=2, default = 0)
    inventory = models.PositiveIntegerField(validators=[MaxValueValidator(10000)])
                                             