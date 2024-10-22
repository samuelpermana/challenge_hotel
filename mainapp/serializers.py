from rest_framework import serializers
from .models import Guests, Rooms, Transactions

class GuestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = '__all__'

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
