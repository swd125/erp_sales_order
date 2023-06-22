from rest_framework import generics

from apis.models import PriceList
from apis.serializers import PriceListSerializer, dynamic_model_create_serializer


class PriceListList(generics.ListCreateAPIView):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            # self.serializer_class = CustomerCreateSerializer
            self.serializer_class = dynamic_model_create_serializer(PriceList)
        return self.serializer_class


class PriceListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer

