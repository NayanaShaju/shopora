from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_user,name='login_user'),
    path('register_user/',views.register_user,name='register_user'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit'),
    path('home/',views.home,name='home'),
    path('add_to_cart/<int:id>',views.add_to_cart,name='addcart'),
    path('cart/',views.cart,name='cart'),
    path('add_to_wishlist/<int:id>',views.add_to_wishlist,name='addwish'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('delete_w/<int:id>',views.delete_w,name='wdelete'),
    path('delete_c/<int:id>',views.delete_c,name='cdelete'),
    path('increase_quantity/<int:id>', views.increase_quantity, name='increase'),
    path('decrease_quantity/<int:id>', views.decrease_quantity, name='decrease'),
    path('order_confirm/',views.order_confirm,name='corder')
]
