# backend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('beneficiaries/', views.beneficiary_list, name='beneficiary_list'),
    path('beneficiaries/<int:pk>/', views.beneficiary_detail, name='beneficiary_detail'),
]
