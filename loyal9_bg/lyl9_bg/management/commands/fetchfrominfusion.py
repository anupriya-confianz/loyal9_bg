from django.core.management.base import BaseCommand, CommandError
from lyl9_bg.infusionsoft.connector import InfusionsoftApiConnector

class Command(BaseCommand):

    def handle(self, *args, **options):
        connector = InfusionsoftApiConnector()
        connector.sync()
