from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Beneficiary
from .serializers import BeneficiarySerializer


@csrf_exempt
def beneficiary_list(request):
    if request.method == 'GET':
        beneficiaries = Beneficiary.objects.all()
        serializer = BeneficiarySerializer(beneficiaries, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = BeneficiarySerializer(data=data)

        if serializer.is_valid():
            beneficiary = serializer.save()
            return JsonResponse({'id': beneficiary.id}, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def beneficiary_detail(request, pk):
    beneficiary = get_object_or_404(Beneficiary, pk=pk)

    if request.method == 'GET':
        serializer = BeneficiarySerializer(beneficiary)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = BeneficiarySerializer(beneficiary, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Beneficiary updated successfully'})
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        beneficiary.delete()
        return JsonResponse({'message': 'Beneficiary deleted successfully'}, status=204)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
