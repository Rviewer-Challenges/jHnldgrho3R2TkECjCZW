from django.core.management.base import BaseCommand
from rviewer_unit_converter.services.unit_converter import UnitConverterService
from rviewer_unit_converter.services.unit_converter_naming import UnitConverterNamingService


class Command(BaseCommand):
    help = 'List available units'

    def handle(self, *args, **options):
        units = [UnitConverterNamingService.get_encoded_conversion(availaible_unit[0], availaible_unit[1])[0] for availaible_unit in UnitConverterService.available_units()]
        self.stdout.write(", ".join(units))
