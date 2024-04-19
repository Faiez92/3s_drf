from rest_framework import serializers
from .models import Beneficiary


class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        optional_fields = [
            'idtype2',
            'type',
            'account_id',
            'payment_type',
            'country',
            'account_name',
            'swift',
            'currency',
            'postcode',
            'address1',
            'bank_name',
            'bank_address',
            'iban',
            'county',
            'town'
        ]

        for field_name in optional_fields:
            self.fields[field_name].required = False
