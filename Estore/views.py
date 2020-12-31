from django.shortcuts import render
from .models import Products, Images
from cart.forms import QuantityForm


def product_list(request):
    item_list = Products.objects.all()[:10]
    context = []
    for item in item_list:
        context.append([item, Images.objects.filter(product=item)[0]])
    return render(request, 'Estore/product_list.html', {'products': context})


def product_details(request, id):
    product = Products.objects.get(pk=id)
    image = Images.objects.filter(product=product)[0]
    form = QuantityForm()
    return render(request, 'Estore/product_details.html', {'product': product,
                                                           'image': image,
                                                           'form': form})


def test(request):
    return render(request, 'Estore/cart.html')