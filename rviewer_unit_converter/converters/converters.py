from rviewer_unit_converter.models import UnitConversion


class Converter:
    DECIMALS = 4

    def __init__(self, model=None):
        self.model = model  # type: UnitConversion

    @property
    def from_unit(self):
        return self.model.from_unit

    @property
    def to_unit(self):
        return self.model.to_unit

    @property
    def conversion_factor(self):
        return float(self.model.conversion)

    def direct(self, quantity):
        return round(quantity * self.conversion_factor, Converter.DECIMALS)

    def inverse(self, quantity):
        return round(quantity / self.conversion_factor, Converter.DECIMALS)


class FormulaConverter(Converter):
    """
    To be used with units that require a formula to be converted, i.e. celsius to fahrenheit
    """
    def _apply_formula(self, quantity):
        raise NotImplemented()

    def direct(self, quantity):
        return round(self._apply_formula(quantity), Converter.DECIMALS)

    def inverse(self, quantity):
        return round(1 / self._apply_formula(quantity), Converter.DECIMALS)

    @staticmethod
    def unit_identifier():
        raise NotImplemented()
