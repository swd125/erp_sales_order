from django.urls import path
from apis.views.v1.customer import CustomerAPIView, CustomerList, CustomerDetail

from apis.views.v1.item import ItemList, ItemDetail
from apis.views.v1.price_list import PriceListList, PriceListDetail
from apis.views.v1.sales_order import SalesOrderList, SalesOrderDetail
from apis.views.v1.sales_order_items import SalesOrderItemsDetail, SalesOrderItemsList

urlpatterns = [

    # -------------- Customer ----------------
    path('customer/', CustomerList.as_view()),
    path('customer/<int:pk>', CustomerDetail.as_view()),

    # -------------- Item ----------------
    path('item/', ItemList.as_view()),
    path('item/<int:pk>', ItemDetail.as_view()),

    # -------------- PriceList ----------------
    path('price-list/', PriceListList.as_view()),
    path('price-list/<int:pk>', PriceListDetail.as_view()),

    # -------------- SalesOrder ----------------
    path('sales-order/', SalesOrderList.as_view()),
    path('sales-order/<int:pk>', SalesOrderDetail.as_view()),

    # -------------- SalesOrder ----------------
    path('sales-order-items/', SalesOrderItemsList.as_view()),
    path('sales-order-items/<int:pk>', SalesOrderItemsDetail.as_view()),

]
