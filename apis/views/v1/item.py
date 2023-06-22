from rest_framework import generics

from apis.models import Item
from apis.serializers import ItemSerializer, dynamic_model_create_serializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            # self.serializer_class = CustomerCreateSerializer
            self.serializer_class = dynamic_model_create_serializer(Item)
        return self.serializer_class


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
