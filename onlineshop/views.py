from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import ContactForm

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
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context ={"items": items, "order": order}
    return render(request, "onlineshop/cart.html", context)

def ContactCreate(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.user=request.user
            form.save()

            return render (request, "onlineshop/contactus.html", {
                "message": "Thank you for contacting us!"
 
            })

        else:
            return render (request, "onlineshop/contactus.html")

    return render(request, "onlineshop/contactus.html", {
        "form": ContactForm,
    })
        
    #model = Contact
    #fields = ["first_name", "last_name", "message"]
    #success_url = reverse_lazy("thanks")

def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context ={"items": items, "order": order}
    return render(request, "onlineshop/checkout.html", context)

def updateItem(request):
    return JsonResponse(request,'Item was added', safe=False)
