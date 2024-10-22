
from rest_framework import viewsets
from ..models.transaction_model import Transactions
from mainapp.serializers.transaction_serializer import  TransactionsSerializer



class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

