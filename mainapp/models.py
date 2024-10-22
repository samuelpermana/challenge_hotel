from django.db import models

class Guests(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def _str_(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class Rooms(models.Model):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField()

    def _str_(self):
        return f"{self.name} - {self.price}"

class Transactions(models.Model):
    guest = models.ForeignKey(Guests, related_name='transaction_guest', on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, related_name='transaction_room', on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    transaction_date = models.DateTimeField()

    def _str_(self):
        return f"Transaction {self.id} - Guest: {self.guest} - Room: {self.room}"