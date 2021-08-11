from django.urls import path
from .views import main,ProductListView

urlpatterns = [
    path('', main,name='index'),
    path('products/', ProductListView.as_view(), name='products'),
]

