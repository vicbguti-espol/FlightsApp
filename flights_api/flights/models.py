from django.db import models

# Create your models here.
class Flight(models.Model):
    name = models.CharField(max_length=60)
    departure_date = models.DateField(auto_now_add=True)
    arrival_date = models.DateField()

    def __str__(self):
        return self.name

class User(models.Model):
    pass