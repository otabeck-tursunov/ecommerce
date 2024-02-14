from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryRetrieveAPIView.as_view()),

    path('sub-categories/', SubCategoryListAPIView.as_view()),
    path('sub-categories/<int:pk>/', SubCategoryRetrieveAPIView.as_view()),

    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view())
]
