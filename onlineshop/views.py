from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render (request,"onlineshop/index.html")

def login(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

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
