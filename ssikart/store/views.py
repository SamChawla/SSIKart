from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category

# Create your views here.

def store_home(request, category_slug=None):
    category = None
    products = None
    products_count = 0

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)
    if products:
        products_count = products.count()

    context_data = {
        "products": products,
        "products_count":products_count,
    }
    return render(request, "store/store.html", context_data)


def product_detail(request, category_slug=None, product_slug=None):
    try:
        product_detail = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        print(e)
        raise e
    context_data = {
        "single_product": product_detail
    }
    return render(request, 'store/product_detail.html', context_data)
