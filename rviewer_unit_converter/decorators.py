from django.conf import settings
from rviewer_unit_converter.services.unit_converter_naming import UnitConverterNamingService


def unit_converter():
    def wrapper(cls):
        settings.REGISTERED_FORMULA_CONVERTERS[
            UnitConverterNamingService.get_encoded_conversion(cls.FROM_UNIT.lower(), cls.TO_UNIT.lower())[0]
        ] = cls
        return cls
    return wrapper
