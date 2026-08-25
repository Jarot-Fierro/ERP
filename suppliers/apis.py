from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from suppliers.models import Supplier


def api_suppliers_details(request):
    pk = request.GET.get('supplier')
    supplier = get_object_or_404(Supplier, id=pk)

    data = {
        'id': supplier.id,
        'name': supplier.name,
        'legal_name': supplier.legal_name,
        'address': supplier.address,
        'city': supplier.city,
        'state_province': supplier.state_province,
        'country': supplier.country.name,
        'zip_code': supplier.zip_code,
        'email': supplier.email,
        'contact_name': supplier.contact_name,
        'payment_terms': supplier.payment_terms,
        'currency': supplier.currency.name,
    }

    return JsonResponse(data)
