from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view()),

    path('sub-categories/', SubCategoriesAPIView.as_view()),
    path('sub-categories/<int:pk>/', SubCategoryRetrieveAPIView.as_view()),

    path('owners/<int:pk>/', OwnerRetrieveAPIView.as_view()),

    path('products/', ProductsAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view()),

    path('products/<int:pk>/images/', ProductImageAPIView.as_view()),
]
