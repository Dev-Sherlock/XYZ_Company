from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from .filters import *
from .models import Product

class ProductListView(ListView):
    model = Product
    paginate_by = 20
    template_name = 'product_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

def main(request):
    return render(request,'company_app/index.html')


