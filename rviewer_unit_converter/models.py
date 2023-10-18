from django.db import models
from django.db.models import Q


class UnitConversion(models.Model):
    from_unit = models.CharField(max_length=20, null=None, blank=None)
    to_unit = models.CharField(max_length=20, null=None, blank=None)
    conversion = models.DecimalField(default=0, decimal_places=6, max_digits=12)

    @staticmethod
    def get_unit_conversion(from_unit, to_unit):
        converter = UnitConversion.objects \
            .filter(Q(from_unit=from_unit, to_unit=to_unit) | Q(from_unit=to_unit, to_unit=from_unit)) \
            .last()  # type: UnitConversion
        return converter

    def __str__(self):
        return "{}/{}".format(self.from_unit, self.to_unit)
