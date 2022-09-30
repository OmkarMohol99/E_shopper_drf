from django.urls import path
from . import views


urlpatterns = [
    path('expense/', views.Expense_Balancesheet_Viewset.as_view(), name='expense')
]