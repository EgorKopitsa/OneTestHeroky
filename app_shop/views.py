from django.shortcuts import render

# Create your views here.
from django.views import View

from app_shop.models import Product


class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'app_shop/index.html', context=context)
