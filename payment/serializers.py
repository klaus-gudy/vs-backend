from .models import Payment
from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
    accountNumber = serializers.CharField(source='phone_number')
    class Meta:
        model = Payment
        fields = ["accountNumber","amount", "currency", "externalId", "provider" ]
        