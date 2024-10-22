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
    guest = GuestsSerializer(read_only=True)
    room = RoomsSerializer(read_only=True)
    guest_id = serializers.IntegerField(write_only=True, required=True)
    room_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Transactions
        fields = '__all__'

    def create(self, validated_data):
        guest_id = validated_data.pop('guest_id')
        room_id = validated_data.pop('room_id')

        transaction = Transactions.objects.create(guest_id=guest_id, room_id=room_id, **validated_data)
        return transaction
