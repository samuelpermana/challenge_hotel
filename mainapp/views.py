from rest_framework import viewsets
from .models import Guests, Rooms, Transactions
from .serializers import GuestsSerializer, RoomsSerializer, TransactionsSerializer

class GuestsViewSet(viewsets.ModelViewSet):
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer

class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    