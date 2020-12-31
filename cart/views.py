from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse
from .forms import QuantityForm
from cart.cart import Cart
from Estore.models import Products, Images
from django.contrib import messages
from .forms import QuantityForm


def cart_view(request):
    cart = Cart(request)
    if request.method == "POST":
        form = QuantityForm(request.POST)
        if form.is_valid():
            cart.set_quantity(product=form.data['product_id'], quantity=int(form.data['quantity']))

    cart_model = []
    for key, value in cart.cart.items():
        cart_model.append([Products.objects.get(id=int(key)),
                           Images.objects.filter(product=key)[0],
                           value['quantity'],
                           Products.objects.get(id=int(key)).price * value['quantity']])
    return render(request, 'Estore/cart.html', {'cart': cart.cart,
                                                'cart_model':cart_model,
                                                'form': QuantityForm(),
                                                })


def add_item(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = QuantityForm(request.POST)
        if form.is_valid():
            cart.add(product=form.data['product_id'], quantity=int(form.data['quantity']))
            messages.success(request, 'Item has been added to the cart.')
        else:
            messages.warning('We are having an issue adding the item. Please try again.')
        return redirect(Products.objects.get(id=form.data['product_id']).get_absolute_url())


def remove_item(request, product_id):
    cart = Cart(request)
    cart.remove(product=int(product_id))
    return redirect('cart:cart_view')

