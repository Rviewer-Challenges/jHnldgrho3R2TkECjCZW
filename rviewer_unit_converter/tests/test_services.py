from django.test import TestCase
from rviewer_unit_converter.services.unit_converter import UnitConverterService
from rviewer_unit_converter.services.unit_converter_naming import UnitConverterNamingService
from rviewer_unit_converter.converters.factory import ConverterFactory
from rviewer_unit_converter.converters.converters import Converter
from rviewer_unit_converter.exceptions import ConverterNotFound
from unittest.mock import Mock, patch


class UnitConverterTest(TestCase):
    def setUp(self):
        self.converter_model = Mock()
        self.converter_model.from_unit = "m"
        self.converter_model.to_unit = "km"
        self.converter_model.conversion = 0.001
        self.converter = Converter(self.converter_model)

    def test_wrong_units_raise_exception(self):
        with self.assertRaises(AssertionError):
            UnitConverterService._do_conversion_calc("test", 1, self.converter)

    def test_direct_conversion_through_service(self):
        self.assertEquals(UnitConverterService._do_conversion_calc(1, "km", self.converter), 1000)

    def test_inverse_conversion_through_service(self):
        self.assertEquals(UnitConverterService._do_conversion_calc(1, "m", self.converter), 0.001)

    def test_convert_calls_conversion(self):
        with patch.object(ConverterFactory, "get_converter", return_value=self.converter):
            self.assertEquals(UnitConverterService.convert(1, "m", "km"), 0.001)

    def test_convert_raises_if_converter_not_found(self):
        with patch.object(ConverterFactory, "get_converter", return_value=None):
            with self.assertRaises(ConverterNotFound, msg='Conversion not found from m to km'):
                self.assertEquals(UnitConverterService.convert(1, "m", "km"), 0.001)


class UnitConverterNamingTest(TestCase):
    def test_correct_name(self):
        self.assertEquals(UnitConverterNamingService.get_encoded_conversion("test", "test2"),
                          ("test/test2", "test2/test"))
