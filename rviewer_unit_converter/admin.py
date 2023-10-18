from django.contrib import admin
from .models import UnitConversion


class UnitConversionAdmin(admin.ModelAdmin):
    list_display = ('from_unit', 'to_unit', 'conversion')


admin.site.register(UnitConversion, UnitConversionAdmin)
