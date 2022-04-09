from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ImageField



class User(AbstractUser):
    pass

class Article (models.Model):
    article_id=models.IntegerField(primary_key=True, default=1)
    title = models.CharField(max_length=64, null=True, blank=True)
    short_description = models.TextField(default=None, null=True, blank=True)
    description = models.TextField()
    details = models.TextField(default=None, null=True, blank=True)
    price = models.DecimalField(max_digits=64, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

@property
def imageURL(self):
    try:
       url = self.image.url
    except:
        url =''
    return url 


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False) 
    transaction_id=models.CharField(max_length=64, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    article=models.ForeignKey(Article, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity=models.IntegerField(default=0, null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.article.price * self.quantity
        return total