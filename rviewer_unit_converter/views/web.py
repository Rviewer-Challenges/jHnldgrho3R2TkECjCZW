from django.views.generic import ListView
from ..models import UnitConversion
from ..services.unit_converter import UnitConverterService


class IndexView(ListView):
    model = UnitConversion
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['units'] = UnitConverterService.available_units()
        return context_data
