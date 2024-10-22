
from django.db import models
from .guest_model import Guests
from .room_model import Rooms

class Transactions(models.Model):
    guest = models.ForeignKey(Guests, related_name='transaction_guest', on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, related_name='transaction_room', on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    transaction_date = models.DateTimeField()

    def _str_(self):
        return f"Transaction {self.id} - Guest: {self.guest} - Room: {self.room}"