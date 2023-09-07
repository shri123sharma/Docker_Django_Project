from .models import Order, OrderStatus, Payment
from .exceptions import InvalidDataException, ServiceException, ObjectNotFoundException


def get_order_by_id(order_id: int) -> Order:
    try:
        order=Order.objects.get(id=order_id)
        return order
    except Order.DoesNotExist:
        raise ObjectNotFoundException("Invalid order object")
    except Exception as e:
        raise ServiceException("Error in retrieving order object")
    

def save_order(order: Order):
    order.status =OrderStatus.NEW
    order.save()
    
    
def dispatch_order(order: Order):
    if order.status != OrderStatus.NEW.name: 
        raise InvalidDataException("Only new orders can be dispatched")
    
    order.status = OrderStatus.DISPATCHED
    order.save()
    
    
def process_payment(order: Order, amount): 
    if order.status != OrderStatus.DISPATCHED.name:
        raise InvalidDataException("Only dispatched orders can be paid")
    
    if order.amount != amount:
        raise InvalidDataException("Order value and payment amount does not match")
    
    already_paid = Payment.objects.filter(order_id=order.id)
    
    if already_paid:
        raise InvalidDataException("Order already has a payment attached")
    
    payment=Payment(order=order, amount=amount)
    payment.save()
    order.payment = payment
    order.status = OrderStatus.DELIVERED
    order.save()
    
    return payment
