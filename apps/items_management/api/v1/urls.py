from django.urls import path
from .views import (CreateCategoryAPIView, GetCategoryAPIView,
                    CategoryDetailAPIView, CategoryDeleteAPIView,
                    CategoryUpdateAPIView, ProductUpdateAPIView,
                    ProductDeleteAPIView, ProductDetailAPIView,
                    GetProductAPIView, CreateProductAPIView,
                    ProductsByCategoryAPIView)

urlpatterns = [
    path('get_category/', GetCategoryAPIView.as_view()),
    path('create_category/', CreateCategoryAPIView.as_view()),
    path('get_category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('delete_category/<int:pk>/', CategoryDeleteAPIView.as_view()),
    path('update_category/<int:pk>/', CategoryUpdateAPIView.as_view()),

    path('get_product/', GetProductAPIView.as_view()),
    path('create_product/', CreateProductAPIView.as_view()),
    path('get_product/<int:pk>/', ProductDetailAPIView.as_view()),
    path('delete_product/<int:pk>/', ProductDeleteAPIView.as_view()),
    path('update_product/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('products/', ProductsByCategoryAPIView.as_view()),

]
