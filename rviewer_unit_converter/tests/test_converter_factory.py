from django.test import TestCase
from django.conf import settings
from unittest.mock import Mock, patch

import rviewer_unit_converter.converters.converters
from rviewer_unit_converter.converters.factory import ConverterFactory
from rviewer_unit_converter.converters.temperature import FahrenheitToCelsiusConverter
from rviewer_unit_converter.models import UnitConversion


class ConverterFactoryAlternateNameTest(TestCase):
    def setUp(self) -> None:
        settings.REGISTERED_FORMULA_CONVERTERS = {
            'km/m': 'found_km_m'
        }

    def test_alternate_name_returns_class_if_direct_name_found(self):
        self.assertEquals(ConverterFactory._get_alternate_class_name("km", "m"), 'found_km_m')

    def test_alternate_name_returns_class_if_reverse_name_found(self):
        self.assertEquals(ConverterFactory._get_alternate_class_name("m", "km"), 'found_km_m')

    def test_alternate_name_returns_none_if_no_name_found(self):
        self.assertIsNone(ConverterFactory._get_alternate_class_name("fm", "ft"))


class ConverterFactoryTest(TestCase):
    def setUp(self) -> None:
        settings.REGISTERED_FORMULA_CONVERTERS = {
            'km/m': FahrenheitToCelsiusConverter
        }

    def test_get_converter_returns_none_if_no_converter_is_found(self):
        with patch.object(UnitConversion, 'get_unit_conversion', return_value=None):
            self.assertIsNone(ConverterFactory.get_converter("fm", "tm"))

    def test_get_converter_retruns_alternate_converter_if_alternate_is_found(self):
        with patch.object(UnitConversion, 'get_unit_conversion', return_value=UnitConversion()):
            self.assertIsInstance(ConverterFactory.get_converter("km", "m"), FahrenheitToCelsiusConverter)

    def test_get_converter_returns_converter(self):
        with patch.object(UnitConversion, 'get_unit_conversion', return_value=UnitConversion()):
            self.assertIsInstance(ConverterFactory.get_converter("rm", "m"),
                                  rviewer_unit_converter.converters.converters.Converter)
