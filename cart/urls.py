from django.urls import path
from . import views


app_name = "cart"

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('cart_add/', views.add_item, name='cart_add'),
    path('cart_remove_item/<int:product_id>/', views.remove_item, name='cart_remove_item'),
]