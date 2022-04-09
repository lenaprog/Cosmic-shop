from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("checkout", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name="update_item"),
    path("cart/", views.cart, name="cart"),
    path("<str:article_title>", views.article, name="article_title"),
    
    
    
]