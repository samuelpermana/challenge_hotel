from rest_framework import serializers
from ..models.transaction_model import Transactions


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
