from django.views.generic import DetailView
from django.http.response import JsonResponse
from ..services.unit_converter import UnitConverterService


class ApiView(DetailView):
    def get(self, request, *args, **kwargs):
        status = 200
        try:
            result = UnitConverterService.convert(
                request.GET.get('units'), request.GET.get('from_unit'), request.GET.get('to_unit')
            )
            data = {'result': result}
        except Exception as e:
            status = 400
            data = {'errors': [str(e)]}
        return JsonResponse(data, status=status)
