from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from safedelete import SOFT_DELETE_CASCADE
from apis.serializers import CustomerSerializer, CustomerDetailSerializer, CustomerCreateSerializer, \
    dynamic_model_create_serializer
from apis.models import Customer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY
from drf_yasg import openapi


class CustomerAPIView(APIView):
    serializer_classes = [CustomerSerializer]

    def get_serializer_class(self):
        print("get_serializer_class >>> ", self.response)
        # if self.request.us:
        #     return FullAccountSerializer

    @swagger_auto_schema(responses={200: CustomerSerializer(many=True)})
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CustomerDetailSerializer)
    def post(self, request):
        serializer = CustomerDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        serializer = CustomerCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # print(serializer_class)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            # self.serializer_class = CustomerCreateSerializer
            self.serializer_class = dynamic_model_create_serializer(Customer)
        return self.serializer_class


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # lookup_field = 'id'


