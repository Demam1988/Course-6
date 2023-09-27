from django.core.management import BaseCommand
from mailings.services import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_email()
