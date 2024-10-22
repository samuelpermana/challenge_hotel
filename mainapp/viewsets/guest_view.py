
from rest_framework import viewsets
from rest_framework.decorators import action
from ..models.room_model import  Rooms
from ..models.guest_model import Guests
from ..models.transaction_model import Transactions
from mainapp.serializers.guest_serializer import GuestsSerializer
from mainapp.serializers.transaction_serializer import  TransactionsSerializer
from rest_framework.response import Response
from django.utils import timezone


class GuestsViewSet(viewsets.ModelViewSet):
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    @action(detail=False, methods=['get'], url_path="grouped-transaction")
    def grouped_transaction(self, request):
        guests = Guests.objects.all()
        data = []

        now = timezone.now()
        for guest in guests:
            transactions = Transactions.objects.filter(guest=guest)
            grouped_transactions = {
                "incoming": [],
                "active": [],
                "past": []
            }
            for transaction in transactions:
                if transaction.check_in_date > now:
                    grouped_transactions['incoming'].append(TransactionsSerializer(transaction).data)
                elif transaction.check_in_date <= now <= transaction.check_out_date:
                    grouped_transactions['active'].append(TransactionsSerializer(transaction).data)
                else:
                    grouped_transactions['past'].append(TransactionsSerializer(transaction).data)

            guest_data = GuestsSerializer(guest).data
            guest_data['transactions'] = grouped_transactions
            data.append(guest_data)
        return Response(data)
