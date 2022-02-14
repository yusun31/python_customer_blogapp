from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.EmailField()
    gender = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '(' + str(self.id) + ')'
