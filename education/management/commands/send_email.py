from django.core.management import BaseCommand

from education.tasks import send_mail_task


class Command(BaseCommand):
    help = "Send email"

    def handle(self, *args, **options):
        send_mail_task.delay()
