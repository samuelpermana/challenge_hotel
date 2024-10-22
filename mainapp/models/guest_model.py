
from django.db import models

class Guests(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def _str_(self):
        return f"{self.first_name} {self.last_name} ({self.email})"