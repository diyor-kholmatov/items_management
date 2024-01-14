from rest_framework import serializers
from apps.items_management.models import CategoryItems, ProductName


class CategoryItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryItems
        fields = '__all__'


class ProductNameSerializers(serializers.ModelSerializer):
    category = CategoryItemsSerializers()

    class Meta:
        model = ProductName
        fields = ('id', 'product_name', 'category', 'created_at', 'updated_at',)
