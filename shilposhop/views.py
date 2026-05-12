from django.shortcuts import render
from products_app.models import Product, Category


def home(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    # Featured: first 8 products
    featured = products[:8]

    return render(request, 'home.html', {
        'products': featured,
        'categories': categories,
        'total_products': products.count(),
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
