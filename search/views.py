from django.shortcuts import render
from products.models import Product

# Create your views here.
def do_search(request):
    """
    We have the model called Product.objects.filter this is a build-in function
    the (name__icontains=request.Get['q']) this will get whatever 'q' search parameter returns 
    from the form
    """
    products = Product.objects.filter(name__icontains=request.Get['q'])
    return render(request, "products.html", {"products": products})
