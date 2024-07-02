from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login/', views.login, name='login'),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('product/<int:pk>/', views.productDetail, name="product_detail"),
    path('privacy-policy/', views.privacy_policy, name="privacy-policy"),
    path('about', views.about, name='about'),
    path('update-cart/', views.updateItem, name='update_cart'),  # Corrected this line
    path('subscribe/', views.subscribe, name='subscribe'),
]
