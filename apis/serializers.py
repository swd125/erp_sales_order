from collections import OrderedDict

from django.db import transaction
from django.forms import model_to_dict
from django.utils.decorators import method_decorator
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from apis.models import Customer, Item, PriceList, SalesOrder, SalesOrderItems
from utils.make_naming_series import make_naming_series, get_naming_series


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerCreateSerializer(serializers.ModelSerializer):
    series_number = serializers.CharField(write_only=True, default="Customer-.#####")

    class Meta:
        model = Customer
        # fields = "__all__"
        # fields = ['customer_name', 'series_number']
        extra_kwargs = {'series_number': {'write_only': True}}
        exclude = ['name']
        # read_only_fields = ['series_number']

    def to_internal_value(self, data):
        series_number = data['series_number']
        make_series = make_naming_series(series_number)
        get_naming = get_naming_series(make_series)
        data['name'] = get_naming
        del data['series_number']
        return data

    def to_representation(self, instance):
        clean_data = instance.__dict__
        del clean_data['_state']
        ret = clean_data
        return ret


class CustomerDetailSerializer(serializers.ModelSerializer):
    series_number = serializers.CharField(write_only=True, default="Customer-.#####", )

    class Meta:
        model = Customer
        fields = ['id', 'customer_name', 'series_number']

    # Hook Level 1
    def to_internal_value(self, data):
        series_number = data['series_number']
        make_series = make_naming_series(series_number)
        get_naming = get_naming_series(make_series)
        data['name'] = get_naming
        del data['series_number']
        return data

    # Hook Level 2
    def validate(self, data):
        # data = super().validate(data)
        return data

    # Hook Level 3
    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    # Hook Level 4
    def to_representation(self, instance):
        ret = {
            'id': instance.id,
            'name': instance.name,
            'customer_name': instance.customer_name,
            'created_at': instance.created_at,
        }
        return ret


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def validate(self, attrs):
        print("attrs >>> ", attrs)
        print("self >>> ", self.context['request'].method)
        return attrs


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = '__all__'


class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = '__all__'


class SalesOrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderItems
        fields = '__all__'


@method_decorator(name="create", decorator=transaction.atomic())
def dynamic_model_create_serializer(model_class):
    model_name = model_class._meta.model_name
    model_default_series = model_name.capitalize()

    class ModelCreateSerializer(serializers.ModelSerializer):
        series_number = serializers.CharField(write_only=True, default=f"{model_default_series}-.#####")

        class Meta:
            model = model_class
            extra_kwargs = {'series_number': {'write_only': True}}
            exclude = ['name']
            ref_name = model_name

        def to_internal_value(self, data):
            # print("to_internal_value >>> ", self.get_fields())
            for field, field_type in self.get_fields().items():
                if isinstance(field_type, serializers.PrimaryKeyRelatedField):
                    # print("field >>> ,", field_type.get_queryset().get(pk=1), type(field_type))
                    model_foreignkey = field_type.get_queryset().get(pk=data[field])
                    # print("model_foreignKey >>>> ", model_foreignKey)
                    data[field] = model_foreignkey
                if isinstance(field_type, serializers.DecimalField):
                    # pass
                    print("DecimalField >>> ", data[field])
                    print("field >>> ,", field_type, type(field_type))
                    # precision = round(data[field], field_type.decimal_places)
                    # print("precision >>> ,", precision)

            series_number = data['series_number']
            make_series = make_naming_series(series_number)
            get_naming = get_naming_series(make_series)
            data['name'] = get_naming
            del data['series_number']
            return data

        def to_representation(self, instance):
            clean_data = instance.__dict__
            del clean_data['_state']
            ret = clean_data
            return ret

    return ModelCreateSerializer
