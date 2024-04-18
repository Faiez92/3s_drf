# backend/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Beneficiary

@csrf_exempt
def beneficiary_list(request):
    if request.method == 'GET':
        beneficiaries = list(Beneficiary.objects.values())
        print('55555555555550', beneficiaries)
        return JsonResponse(beneficiaries, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        beneficiary = Beneficiary.objects.create(
            name=data['name'],
            company=data['company'],
            bank_country=data['bank_country'],
            account_number=data['account_number']
        )
        return JsonResponse({'id': beneficiary.id}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def beneficiary_detail(request, pk):
    beneficiary = get_object_or_404(Beneficiary, pk=pk)

    if request.method == 'GET':
        beneficiary_data = {
            'id': beneficiary.id,
            'name': beneficiary.name,
            'company': beneficiary.company,
            'bank_country': beneficiary.bank_country,
            'account_number': beneficiary.account_number
        }
        return JsonResponse(beneficiary_data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        beneficiary.name = data['name']
        beneficiary.company = data['company']
        beneficiary.bank_country = data['bank_country']
        beneficiary.account_number = data['account_number']
        beneficiary.save()
        return JsonResponse({'message': 'Beneficiary updated successfully'})

    elif request.method == 'DELETE':
        beneficiary.delete()
        return JsonResponse({'message': 'Beneficiary deleted successfully'}, status=204)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
