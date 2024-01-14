from django.db import models
from apps.base.models import BaseModel


class CategoryItems(BaseModel):
    category_name = models.CharField(max_length=50)


class ProductName(BaseModel):
    product_name = models.CharField(max_length=60)
    category = models.ForeignKey(CategoryItems, on_delete=models.CASCADE)
