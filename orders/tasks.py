from Myshop import celery_app
from django.core.mail import send_mail
from .models import Order


@celery_app.task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {},\n\n You have successfully placed an order.\n Your  order id is {}. '.format(order.first_name,
                                                                                                    order.id)
    mail_send = send_mail(subject, message, 'kedr_test_smtp@mail.ru', [order.email])
    return mail_send
