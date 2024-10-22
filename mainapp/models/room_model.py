
from django.db import models

class Rooms(models.Model):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField()

    def _str_(self):
        return f"{self.name} - {self.price}"
