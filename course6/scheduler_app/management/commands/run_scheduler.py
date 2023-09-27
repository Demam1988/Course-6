from django.core.management.base import BaseCommand
from scheduler_app.scheduler import scheduler


class Command(BaseCommand):
    help = 'Runs the APScheduler'

    def handle(self, *args, **options):
        scheduler.start()
