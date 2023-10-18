from rviewer_unit_converter.decorators import unit_converter
from rviewer_unit_converter.converters.converters import FormulaConverter
from rviewer_unit_converter.services.unit_converter_naming import UnitConverterNamingService


@unit_converter()
class FahrenheitToCelsiusConverter(FormulaConverter):
    FROM_UNIT = "Fahrenheit"
    TO_UNIT = "Celsius"

    @staticmethod
    def unit_identifier():
        return UnitConverterNamingService.get_encoded_conversion(
            FahrenheitToCelsiusConverter.FROM_UNIT,
            FahrenheitToCelsiusConverter.TO_UNIT
        )

    def _apply_formula(self, quantity):
        return (quantity - 32) * 5 / 9

    def inverse(self, quantity):
        return (quantity * (9 / 5)) + 32
