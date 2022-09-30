import imp
from rest_framework import serializers
from .models import Expense_Balancesheet


class Expense_BalancesheetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expense_Balancesheet
        fields = '__all__'


    def create(self, validated_data):
        return Expense_Balancesheet.objects.create(**validated_data)