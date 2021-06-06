from celery import shared_task
from django.core import mail
from django.core.mail import send_mail


@shared_task
def send_mail_task():
    with mail.get_connection() as connection:
        return send_mail(
            'Sending email from celery',
            'Here we go.',
            'from@example.com',
            ['balancy@gmail.com'],
            connection=connection,
        )
