from django.test import TestCase
from rviewer_unit_converter.converters.temperature import FahrenheitToCelsiusConverter
from unittest.mock import Mock


class FahrenheitToCelsiusConverterTest(TestCase):
    def setUp(self):
        ...

    def test_fahrenheit_to_celsius_conversion(self):
        model = Mock()
        converter = FahrenheitToCelsiusConverter(model)
        self.assertEquals(0, converter.direct(32))
        self.assertAlmostEqual(-9.4444, converter.direct(15), 5)
        self.assertAlmostEqual(10, converter.direct(50), 1)

    def test_celsius_to_fahrenheit_conversion(self):
        model = Mock()
        converter = FahrenheitToCelsiusConverter(model)
        self.assertEquals(32, converter.inverse(0))
        self.assertAlmostEqual(15, converter.inverse(-9.4444), 2)
        self.assertAlmostEqual(50, converter.inverse(10), 1)
