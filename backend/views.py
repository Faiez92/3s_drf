# backend/views.py
import json
import os

import requests
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Beneficiary

THREE_S_API_KEY = os.getenv("THREE_S_API_KEY")
THREE_S_BASE_URL = 'https://demo.api.3s.money/v1.1'

@csrf_exempt
def beneficiary_list(request):
    if request.method == 'GET':
        beneficiaries = list(Beneficiary.objects.values())
        return JsonResponse(beneficiaries, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        beneficiary = Beneficiary.objects.create(
            name=data['name'],
            company=data['company'],
            bank_country=data['bank_country'],
            account_number=data['account_number']
        )

        # Call 3S Money API to create the beneficiary
        api_url = f'{THREE_S_BASE_URL}/beneficiaries'
        headers = {'Authorization': f'Bearer {THREE_S_API_KEY}', 'Content-Type': 'application/json'}
        api_data = {
            'name': beneficiary.name,
            'company': beneficiary.company,
            'bank_country': beneficiary.bank_country,
            'account_number': beneficiary.account_number
        }
        response = requests.post(api_url, headers=headers, json=api_data)

        if response.status_code != 201:
            return JsonResponse({'error': 'Failed to create beneficiary via API'}, status=500)

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

        # Call 3S Money API to update the beneficiary
        api_url = f'{THREE_S_BASE_URL}/beneficiaries/{pk}'
        headers = {'Authorization': f'Bearer {THREE_S_API_KEY}', 'Content-Type': 'application/json'}
        api_data = {
            'name': beneficiary.name,
            'company': beneficiary.company,
            'bank_country': beneficiary.bank_country,
            'account_number': beneficiary.account_number
        }
        response = requests.put(api_url, headers=headers, json=api_data)

        if response.status_code != 200:
            return JsonResponse({'error': 'Failed to update beneficiary via API'}, status=500)

        return JsonResponse({'message': 'Beneficiary updated successfully'})
    elif request.method == 'DELETE':
        beneficiary.delete()

        # Call 3S Money API to delete the beneficiary
        api_url = f'{THREE_S_BASE_URL}/beneficiaries/{pk}'
        headers = {'Authorization': f'Bearer {THREE_S_API_KEY}'}
        response = requests.delete(api_url, headers=headers)

        if response.status_code != 204:
            return JsonResponse({'error': 'Failed to delete beneficiary via API'}, status=500)

        return JsonResponse({'message': 'Beneficiary deleted successfully'}, status=204)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
