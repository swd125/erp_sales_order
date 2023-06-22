from rest_framework import generics

from apis.models import SalesOrder
from apis.serializers import SalesOrderSerializer, dynamic_model_create_serializer


class SalesOrderList(generics.ListCreateAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            # self.serializer_class = CustomerCreateSerializer
            self.serializer_class = dynamic_model_create_serializer(SalesOrder)
        return self.serializer_class


class SalesOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
