from celery import shared_task
from django.core import mail
from django.core.mail import send_mail


@shared_task
def send_mail_task(subject, message, from_mail, to_mail):
    with mail.get_connection() as connection:
        return send_mail(
            subject,
            message,
            from_mail,
            [to_mail],
            connection=connection,
        )
