from django.urls import path
from .views import AccountView, PaymentView

urlpatterns = [
    path('accounts/', AccountView.as_view(), name='account-list'),
    path('accounts/<int:id>/', AccountView.as_view(), name='account-detail'),
    path('payments/', PaymentView.as_view(), name='payment-list'),
]
