from django.core.management.base import BaseCommand
from rviewer_unit_converter.services.unit_converter import UnitConverterService


class Command(BaseCommand):
    help = 'Convert from one unit to another'

    def add_arguments(self, parser):
        parser.add_argument('units', type=float, help='Units to convert (i.e. 10)')
        parser.add_argument(
            'from_unit', default=False, help='Source unit (i.e. km)',
        )
        parser.add_argument(
            'to_unit', default=False, help='Destination unit (i.e. m)',
        )

    def handle(self, *args, **options):
        from_unit = options.get('from_unit')
        to_unit = options.get('to_unit')
        try:
            converted = UnitConverterService.convert(options.get('units'), from_unit, to_unit)
            self.stdout.write(f"{options['units']} {from_unit} = {converted} {to_unit}")
        except Exception as e:
            self.stderr.write(str(e))
