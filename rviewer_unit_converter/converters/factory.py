from django.conf import settings
from rviewer_unit_converter.services.unit_converter_naming import UnitConverterNamingService
from rviewer_unit_converter.models import UnitConversion
from rviewer_unit_converter.converters.converters import Converter


class ConverterFactory:
    converters = []

    @staticmethod
    def get_converter(from_unit, to_unit):
        """
        Returns a converter to perform conversion.
        :param from_unit:
        :param to_unit:
        :return:
        """
        converter = None
        converter_model = UnitConversion.get_unit_conversion(from_unit, to_unit)
        converter_alternate_class = ConverterFactory._get_alternate_class_name(from_unit, to_unit)

        if converter_alternate_class and converter_model:
            converter = converter_alternate_class(converter_model)
        elif converter_model:
            converter = Converter(converter_model)
        return converter

    @staticmethod
    def _get_alternate_class_name(from_unit, to_unit):
        converter_class = None
        direct, inverse = UnitConverterNamingService.get_encoded_conversion(from_unit, to_unit)

        if direct in settings.REGISTERED_FORMULA_CONVERTERS:
            converter_class = settings.REGISTERED_FORMULA_CONVERTERS[direct]
        if inverse in settings.REGISTERED_FORMULA_CONVERTERS:
            converter_class = settings.REGISTERED_FORMULA_CONVERTERS[inverse]
        return converter_class
