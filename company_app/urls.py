from django.urls import path
from .views import main,ProductListView

urlpatterns = [
    path('', main),
    path('products/', ProductListView.as_view(), name='products'),
]