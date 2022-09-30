from django.urls import path
from . import views


urlpatterns = [
    path('orders/', views.CreateOrder.as_view()),
    path('invoice1/', views.CreateOrder.as_view()),
    path('invoice1/<int:pk>/', views.CreateOrder.as_view()),
    path('invoice2/', views.CreateInvoice.as_view()),
    path('products/', views.ProductDetails.as_view()),  #added
    path('products/<int:pk>/', views.ProductDetails.as_view()), #added
    path('customer/', views.Customerdetails.as_view()),
]
