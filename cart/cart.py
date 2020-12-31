from Estore.models import Products


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = request.session.get('cart')
        if not cart:
            cart = request.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity):
        if product in self.cart:
            self.cart[product]['quantity'] += quantity
        else:
            self.cart[product] = {'quantity': quantity}
        self.session.modified = True

    def set_quantity(self,product, quantity):
        if product in self.cart:
            self.cart[product]['quantity'] = quantity

    def remove(self, product):
        if str(product) in self.cart:
            del self.cart[str(product)]
        self.session.modified = True

    def clear(self):
        try:
            del self.session['cart']
        except KeyError:
            pass
        self.session.modified = True

