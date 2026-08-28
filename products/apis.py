from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from products.models import Material


def api_materials_details(request, id):
    material = get_object_or_404(Material, id=id)

    data = {
        'id': material.id,
        'name': material.name,
        'unit': material.unit.symbol,
        'description': material.description,
    }

    return JsonResponse(data)
