from rest_framework import generics
from apps.items_management.models import ProductName, CategoryItems
from .serializers import CategoryItemsSerializers, ProductNameSerializers
from .permissions import IsSuperAdminPermissions
from rest_framework.permissions import IsAuthenticated


class GetCategoryAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = CategoryItems.objects.all().order_by('id')
    serializer_class = CategoryItemsSerializers


class CreateCategoryAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = CategoryItems.objects.all()
    serializer_class = CategoryItemsSerializers


class CategoryDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = CategoryItems.objects.all()
    serializer_class = CategoryItemsSerializers


class CategoryUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = CategoryItems.objects.all()
    serializer_class = CategoryItemsSerializers


class CategoryDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = CategoryItems.objects.all()
    serializer_class = CategoryItemsSerializers


class GetProductAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = ProductName.objects.all().order_by('id')
    serializer_class = ProductNameSerializers


class CreateProductAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = ProductName.objects.all()
    serializer_class = ProductNameSerializers


class ProductDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = ProductName.objects.all()
    serializer_class = ProductNameSerializers


class ProductUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = ProductName.objects.all()
    serializer_class = ProductNameSerializers


class ProductDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = ProductName.objects.all()
    serializer_class = ProductNameSerializers


class ProductsByCategoryAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ProductNameSerializers

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        return ProductName.objects.filter(category_id=category_id)
