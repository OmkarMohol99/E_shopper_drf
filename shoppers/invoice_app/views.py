
from django.shortcuts import render
from .serializers import InvoiceSerializers, CustomerOrderSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection
from . import models

# Create your views here.


class CreateOrder(APIView):
    # here we access the particular data of customerorder
    def get(self, request, pk):
        orders = {}
        li = []
        cname = ''
        caddr = ''
        invoiceid = 0
        invoice_date = 0
        tax = 0
        cursor = connection.cursor()
        paymode = ''
        invoice_cus = models.CustomerOrder.objects.filter(customerinvoice=pk)
        for p in models.Customer.objects.raw(f'SELECT c_id,order_id,invoice_id,c_name,invoice_app_product.category_id,product_stock,invoice_app_product.vendor_id,p_id,p_name,p_price,unit,payment_mode,igst,hsn_code,discount,gross_cost,net_amount,quantity,invoice_date FROM invoice_app_customer INNER JOIN invoice_app_customerinvoice ON invoice_app_customer.c_id = invoice_app_customerinvoice.customer_id INNER JOIN invoice_app_customerorder ON invoice_app_customerinvoice.invoice_id = invoice_app_customerorder.customerinvoice_id INNER JOIN invoice_app_product ON invoice_app_customerorder.product_id = invoice_app_product.p_id INNER JOIN invoice_app_discount ON invoice_app_product.discount_id = invoice_app_discount.discount_id INNER JOIN invoice_app_gst ON invoice_app_gst.gst_id = invoice_app_product.gst_id where invoice_app_customerorder.customerinvoice_id = {pk};'):
            print(p.invoice_id, p.c_name, p.p_id, p.category_id, p.vendor_id, p.p_name, p.p_price, p.unit, p.gross_cost, p.igst, p.discount, ((
                (((p.p_price*p.igst)/100)+p.p_price)-p.discount)*p.quantity), p.payment_mode, p.quantity, p.invoice_date, p.hsn_code)
            pro_stock = models.Product.objects.get(pk=p.p_id)
            update_stock = pro_stock.product_stock - p.quantity
            print(pro_stock.product_stock, p.quantity, update_stock)
            cursor = connection.cursor()
            cursor.execute(
                f'''UPDATE invoice_app_product SET product_stock = {update_stock} where p_id = {p.p_id};''')
            paymode = p.payment_mode
            tax = ((p.p_price*p.igst)/100)
            total = (((tax+p.p_price)-p.discount)*p.quantity)
            li.append(total)
            orders[f"order{p.order_id}"] = (
                p.p_id, p.p_name, p.p_price, p.unit, tax, p.quantity, p.discount, p.hsn_code, total, p.payment_mode)
            caddr = p.c_address
            cname = p.c_name
            invoiceid = p.invoice_id
            invoice_date = p.invoice_date
        net_amount = sum(li)
        cursor.execute(
            f'''update invoice_app_customerinvoice SET net_Amount = {net_amount} where invoice_id = {invoiceid};''')
        print(orders)

        print(net_amount)

        # print(invoice_cus)
        serializer = CustomerOrderSerializers(invoice_cus, many=True)
        return Response(data={"status": "updatedss", "invoice_no": invoiceid, "customer name": cname, "customer address": caddr, "date": invoice_date, "data": orders, "net amount": net_amount})


###GET ALL CUSTOMER ORDER DATA ###


    def get(self, request):
        queryset = models.CustomerOrder.objects.all()
        serializer = CustomerOrderSerializers(queryset, many=True)
        return Response(data=serializer.data, status=200)

# here we add the customer order to customerorder table

    def post(self, request):
        serializer = CustomerOrderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)


# here we implement particular order retrive

class CreateCustomerOrder(APIView):
    def get(self, requets, pk):
        try:
            cus_order = models.CustomerOrder.objects.get(pk=pk)
            serializer = CustomerOrderSerializers(cus_order)
            return Response(data=serializer.data, status=200)
        except:
            return Response(data={'message': 'Data Not Found'}, status=400)
