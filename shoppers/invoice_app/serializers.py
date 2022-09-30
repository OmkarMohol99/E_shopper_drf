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
    gst = serializers.SlugRelatedField(
    
        read_only = True,
        slug_field = 'igst'
    )
    discount = serializers.SlugRelatedField(
        read_only = True,
        slug_field = 'discount'
    )
    class Meta:
        model = models.Product
        fields = '__all__'
    
    def update(self, instance, validated_data):
        instance.p_id = validated_data.get('p_id', instance.p_id)
        instance.product_stock = validated_data.get('product_stock', instance.product_stock)
        instance.save()
        return instance


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields ='__all__'

