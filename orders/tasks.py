from asyncio import tasks
from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_cerated(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'You have sucessfully placed an order.' \
              f'your order ID is {order.id}.'
    mail_set = send_mail(subject,
                        message,
                        'admin@e-commerce.com',
                        [order.email])
    return mail_set                          



# Import => apt-get install rabbitmq
# celery -A myshop flower