from rviewer_unit_converter.models import UnitConversion
from rviewer_unit_converter.converters.factory import ConverterFactory
from rviewer_unit_converter.exceptions import ConverterNotFound
from rviewer_unit_converter.converters.temperature import *  # we need to register classes with decorator


class UnitConverterService:
    DECIMAL_FIELDS = 6

    @staticmethod
    def convert(units, from_unit, to_unit):
        converter = ConverterFactory.get_converter(from_unit, to_unit)  # type: rviewer_unit_converter.converters.converters.Converter
        if not converter:
            raise ConverterNotFound("Conversion not found from {} to {}".format(from_unit, to_unit))
        return UnitConverterService._do_conversion_calc(float(units), from_unit, converter)

    @staticmethod
    def _do_conversion_calc(units, from_unit, converter):
        assert isinstance(units, int) or isinstance(units, float), "Units are not neither integer nor float"

        switch_source = converter.from_unit != from_unit
        return converter.inverse(units) if switch_source else converter.direct(units)

    @staticmethod
    def available_units():
        units = UnitConversion.objects.values_list("from_unit", "to_unit")
        return_units = []
        for unit in units:
            return_units.append(unit)
            return_units.append((unit[1], unit[0]))
        return return_units

    @staticmethod
    def find_way_to_conversion(from_units, to_units):
        # TODO: from from_units find way to to_units using recursion
        raise NotImplemented()
