
from django.contrib import admin
from .models import Customer, CustomerInvoice, CustomerOrder, PurchaseOrder, PurchaseOrderDetails, Vendor, Product, Category, GST, Discount, BalanceSheet
from auth_app.models import User
from expenses_app.models import Expense_Balancesheet


# Register your models here.
# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['c_id', 'c_name', 'c_email', 'c_phone', 'c_address']
#     list_filter = ['c_email', 'c_phone', 'c_address']
#     search_fields = ['c_id', 'c_name', 'c_email', 'c_phone', 'c_address']
admin.site.register(Customer)


# @admin.register(CustomerInvoice)
# class CustomerInvoiceAdmin(admin.ModelAdmin):
#     list_display = ['invoice_id', 'c_id', 'payment_mode', 'quantity']
#     list_filter = ['invoice_id', 'c_id', 'payment_mode', 'quantity']
#     search_fields = ['invoice_id', 'c_id', 'payment_mode', 'quantity']
admin.site.register(CustomerInvoice)

# @admin.register(CustomerOrder)
# class CustomerOrderAdmin(admin.ModelAdmin):
#     list_display = ['order_id', 'invoice_id', 'p_id', 'quantity']
#     list_filter = ['order_id', 'quantity']
#     search_fields = ['order_id', 'invoice_id', 'p_id', 'quantity']
admin.site.register(CustomerOrder)


# @admin.register(PurchaseOrder)
# class PurchaseOrderAdmin(admin.ModelAdmin):
#     list_display = ['po_id', 'vender_id', 'p_id']
#     list_filter = ['po_id', 'vender_id', 'p_id']
#     search_fields = ['po_id', 'vender_id', 'p_id']
admin.site.register(PurchaseOrder)

# @admin.register(Vendor)
# class VendorAdmin(admin.ModelAdmin):
#     list_display = ['v_id', 'v_name', 'v_phone', 'v_email', 'v_address', 'v_gst_no']
#     list_filter = ['v_phone', 'v_email', 'v_gst_no']
#     search_fields = ['v_id', 'v_name', 'v_phone', 'v_email', 'v_address', 'v_gst_no']
admin.site.register(Vendor)


# @admin.register(VendorInvoice)
# class VendorInvoice(admin.ModelAdmin):
#     list_display = ['v_invoice_id', 'v_id', 'total_amount', 'date']
#     list_filter = ['v_invoice_id', 'v_id', 'total_amount', 'date']
#     search_fields = ['v_invoice_id', 'v_id', 'total_amount', 'date']

admin.site.register(PurchaseOrderDetails)
admin.site.register(Category)
admin.site.register(GST)
admin.site.register(Discount)
admin.site.register(Product)
admin.site.register(BalanceSheet)
admin.site.register(User)
admin.site.register(Expense_Balancesheet)
