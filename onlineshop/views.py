from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from .models import User, Article

# Create your views here.
def index(request):
    return render (request, "onlineshop/index.html", {
        "articles": Article.objects.all()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "onlineshop/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "onlineshop/login.html")

# view for registering
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "onlineshop/register.html", {
                "message": "Passwords must match.",
                "msg_type": "danger"
            })
        if not username:
            return render(request, "onlineshop/register.html", {
                "message": "Please enter your username.",
                "msg_type": "danger"
            })
        if not email:
            return render(request, "onlineshop/register.html", {
                "message": "Please enter your email.",
                "msg_type": "danger"
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "onlineshop/register.html", {
                "message": "Username already taken.",
                "msg_type": "danger"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    # if GET request
    else:
        return render(request, "onlineshop/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def article(request, article_title):
    article= Article.objects.get(title=article_title)
    return render (request, "onlineshop/article.html", {
        "article": article
    })

def cart(request):
    return render(request, "onlineshop/cart.html")
