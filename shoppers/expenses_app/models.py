from django.db import models
from invoice_app.models import PurchaseOrderDetails, CustomerInvoice
from django.db.models import CASCADE


class Expense_Balancesheet(models.Model):
    bs_id = models.IntegerField(primary_key=True)
    purchaseorderdetails = models.ForeignKey(
    PurchaseOrderDetails, on_delete=CASCADE)
    customerinvoice = models.ForeignKey(CustomerInvoice, on_delete=CASCADE)
    light_bill = models.FloatField()
    emp_salary = models.FloatField()
    monthly_rent = models.FloatField()
    miscellaneous = models.FloatField()
    bs_date = models.DateField()

    def __str__(self):

        return f"{self.bs_id}"
