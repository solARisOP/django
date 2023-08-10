from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.

# all corresponding functions are as below
def index(request):
    context = { #variable names and there corresponding contents we wanna display through the view
        "var1" : "rao is the greatest",
        "var2" : "he is the best"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        member = Contact(name = name, email= email, phone = phone, desc = desc, date = datetime.today())
        member.save()
        messages.success(request, "Your message has been sent !")
    return render(request, "contact.html")
