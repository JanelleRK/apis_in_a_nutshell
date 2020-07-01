from django.core.management.base import BaseCommand, CommandError
from api.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'Creates a shoe type and shoe color'

    def handle(self, *args, **options):
        style = [
            'Sneaker',
            'Boot',
            'Sandal',
            'Dress',
            'Other'
        ]
        color_name = [
            'Red',
            'Orange',
            'Yellow',
            'Green',
            'Blue',
            'Indigo',
            'Violet',
            'White',
            'Black'
        ]
        try:
            for shoe_type in style:
                ShoeType.objects.create(style=shoe_type)
            for color in color_name:
                ShoeColor.objects.create(color_name=color)
            print("Object created")
        except:
            raise CommandError("Oops.")




