
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
