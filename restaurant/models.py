from django.db import models
from django.core.validators import MinValueValidator


class TableType(models.Model):[
   
]


class Booking(models.Model):
   TABLE_TYPE = [
      ("pvt", "Privet"),
      ("pub", "Public"),
      ("win", "Window Side")
   ]
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   Table_Type = models.CharField(max_length=3, choices=TABLE_TYPE, default='pvt')
   guest_number = models.IntegerField(validators=[MinValueValidator(1)])
   comment = models.CharField(max_length=1000)

   def __str__(self, get):
      return self.first_name + ' ' + self.last_name



class Menu(models.Model):
   name = models.CharField(max_length=255)
   price = models.IntegerField()
   description = models.CharField(max_length=1000, blank=True, null=True)

   def __str__(self):
      return self.name