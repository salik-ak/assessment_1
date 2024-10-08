from django.urls import path
from . import views
from .views import ProductListCreate, CategoryListCreate,CategoryDetailUpdateDelete, ProductDetailUpdateDelete
urlpatterns = [
    path('categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailUpdateDelete.as_view(), name='category-detail-update-delete'),
    path('products/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductDetailUpdateDelete.as_view(), name='product-detail-update-delete'),
]
