from django.shortcuts import render
from .serializers import Expense_BalancesheetSerializers
from .models import Expense_Balancesheet
from rest_framework.views import APIView
from rest_framework.response import Response



class Expense_Balancesheet_Viewset(APIView):
    def post(self, request):
        serializer = Expense_BalancesheetSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)


    def get(self, request):
        data = Expense_Balancesheet.objects.all()
        serializer = Expense_BalancesheetSerializers(data, many=True)
        return Response(data=serializer.data, status=200)
