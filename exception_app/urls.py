from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:order_id>/dispatch/', OrderDispatchView.as_view(), name='dispatch'),
    path('orders/<int:order_id>/payments/', OrderPaymentView.as_view(), name='payments'),
    
]
