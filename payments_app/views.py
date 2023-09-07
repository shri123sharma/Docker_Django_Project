from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Payment
from .serializers import AccountSerializer, PaymentSerializer
from django.shortcuts import get_object_or_404
from json.decoder import JSONDecodeError

class AccountView(APIView):
    def post(self, request):
        account = Account.objects.create()
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, id):
        account = get_object_or_404(Account,id=id)
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PaymentView(APIView):
    
    def post(self, request):
        try:
            account_id = request.data.get("account")
            amount = request.data.get("amount")
            try:
                account = Account.objects.get(id=account_id)
                
            except Account.DoesNotExist:
                return Response({"error": "Account does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            
            if int(amount) > 0:
                payment = Payment.objects.create(account=account, amount=int(amount))
                
                account_serializer = AccountSerializer(account)
                account_balance = account_serializer.get_balance(account)
                
                account.balance = account_balance
                account.save()
                
                serializer = PaymentSerializer(payment)
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Invalid payment amount"}, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return Response({"error": "JSON decoding error"}, status=status.HTTP_400_BAD_REQUEST)
        
    
    