
from dataclasses import fields
from rest_framework import serializers
from . import models


class InvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerInvoice
        fields = '__all__'


class CustomerOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerOrder
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields ='__all__'

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields ='__all__'