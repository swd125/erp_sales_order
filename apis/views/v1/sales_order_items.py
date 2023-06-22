from rest_framework import generics

from apis.models import SalesOrderItems
from apis.serializers import SalesOrderItemsSerializer, dynamic_model_create_serializer


class SalesOrderItemsList(generics.ListCreateAPIView):
    queryset = SalesOrderItems
    serializer_class = SalesOrderItemsSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            # self.serializer_class = CustomerCreateSerializer
            self.serializer_class = dynamic_model_create_serializer(SalesOrderItems)
        return self.serializer_class


class SalesOrderItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesOrderItems
    serializer_class = SalesOrderItemsSerializer
