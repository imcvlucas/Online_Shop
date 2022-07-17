from django.shortcuts import render, get_object_or_404

from .models import Category, Product

# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    content = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'product/list.html', content)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    content = {'product': product}
    return render(request, 'product/detail.html', content)
