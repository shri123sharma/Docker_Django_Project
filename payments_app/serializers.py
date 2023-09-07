from rest_framework import serializers
from .models import Account, Payment
from django.db.models import Sum

class AccountSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField() #Set the default balance to 0
    
    class Meta:
        model = Account
        fields = ['id', 'balance']
        
    def get_balance(self, account):
        payments_sum = Payment.objects.filter(account=account).aggregate(Sum('amount'))['amount__sum']
        return payments_sum or 0  
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'account', 'amount']
        
    

