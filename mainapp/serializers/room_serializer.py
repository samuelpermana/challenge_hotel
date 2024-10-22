from rest_framework import serializers
from ..models.room_model import  Rooms
from ..models.guest_model import Guests
from ..models.transaction_model import Transactions

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'
