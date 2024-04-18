from django.db import models


class Beneficiary(models.Model):
    idtype2 = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    account_id = models.CharField(max_length=100)
    bank_country = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    company = models.CharField(max_length=255)  # Assuming 'company' is the company name
    country = models.CharField(max_length=100)  # Assuming 'country' is the beneficiary country
    account_name = models.CharField(max_length=255)  # Assuming 'account-name' is the beneficiary account name
    swift = models.CharField(max_length=100)  # Assuming 'swift' is the SWIFT/BIC code
    currency = models.CharField(max_length=100)  # Assuming 'currency' is the currency code
    postcode = models.CharField(max_length=100)  # Assuming 'postcode' is the postcode
    address1 = models.CharField(max_length=255)  # Assuming 'address1' is the address line 1
    bank_name = models.CharField(max_length=255)  # Assuming 'bank-name' is the bank name
    bank_address = models.CharField(max_length=255)  # Assuming 'bank-address' is the bank address
    iban = models.CharField(max_length=100)  # Assuming 'iban' is the IBAN
    name = models.CharField(max_length=255)  # Assuming 'name' is the beneficiary name
    county = models.CharField(max_length=255)  # Assuming 'county' is the county
    account_number = models.CharField(max_length=100)  # Assuming 'account-number' is the account number
    town = models.CharField(max_length=255)  # Assuming 'town' is the town/city

    def __str__(self):
        return self.name
