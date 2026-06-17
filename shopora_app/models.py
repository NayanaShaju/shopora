from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class profile_table(models.Model):
        user=models.OneToOneField(User,on_delete=models.CASCADE)
        address=models.CharField(max_length=200)
        contact_number=models.IntegerField()
        def __str__(self):
            return self.user.username
    
class products(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    def __str__(self):
        return self.product_name
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.product.product_name
    
class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    def __str__(self):
        return self.product.product_name