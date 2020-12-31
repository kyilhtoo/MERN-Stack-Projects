from django.urls import path
from . import views

app_name = "Estore"

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('test/', views.test, name='test'),
    path('product_details/<int:id>/', views.product_details, name='product_details'),
]

