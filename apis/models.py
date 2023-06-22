from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from datetime import date


# Create your models here.


class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    original_objects = models.Manager()
    name = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    customer_name = models.CharField(max_length=255)


class Item(BaseModel):
    item_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    uom = models.CharField(max_length=255, blank=True, null=True)


class PriceList(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price_list_type = models.CharField(max_length=255, blank=True, null=True)
    price_list_rate = models.DecimalField(max_digits=6, decimal_places=3)


class SalesOrder(BaseModel):
    posting_date = models.DateField(blank=True, default=date.today())
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=3, decimal_places=3)
    discount_amount = models.DecimalField(max_digits=3, decimal_places=3)
    total_vat = models.DecimalField(max_digits=3, decimal_places=3)
    grand_total = models.DecimalField(max_digits=3, decimal_places=3)


class SalesOrderItems(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=3, decimal_places=3)
    discount_amount = models.DecimalField(max_digits=3, decimal_places=3)
    total_amount = models.DecimalField(max_digits=3, decimal_places=3)


# ---- Utils ----

class SeriesNumber(models.Model):
    naming_series = models.CharField(max_length=255)
    running_number = models.IntegerField(default=1)



