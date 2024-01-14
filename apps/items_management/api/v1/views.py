from rest_framework import generics
from apps.items_management.models import ProductName, CategoryItems
from .serializers import CategoryItemsSerializers, ProductNameSerializers


class GetCategoryAPIView(generics.ListAPIView):
    queryset = CategoryItems.objects.all().order_by('id')
    serializer_class = CategoryItemsSerializers


class CreateCategoryAPIView(generics.CreateAPIView):
    queryset = CategoryItems.objects.all()
    serializer_class = CategoryItemsSerializers


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = CategoryItems.objects.all()
    serializer_class = CategoryItemsSerializers


class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = CategoryItems.objects.all()
    serializer_class = CategoryItemsSerializers


class CategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = CategoryItems.objects.all()
    serializer_class = CategoryItemsSerializers


class GetProductAPIView(generics.ListAPIView):
    queryset = ProductName.objects.all().order_by('id')
    serializer_class = ProductNameSerializers


class CreateProductAPIView(generics.CreateAPIView):
    queryset = ProductName.objects.all()
    serializer_class = ProductNameSerializers


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = ProductName.objects.all()
    serializer_class = ProductNameSerializers


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = ProductName.objects.all()
    serializer_class = ProductNameSerializers


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = ProductName.objects.all()
    serializer_class = ProductNameSerializers


class ProductsByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductNameSerializers

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        return ProductName.objects.filter(category_id=category_id)


