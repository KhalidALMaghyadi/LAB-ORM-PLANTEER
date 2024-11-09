from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.
from .models import Contact
from plant .models import Plant

def home_view(request:HttpRequest):

    Plants = Plant.objects.all()[0:3]

    return render(request,'main/home.html',{"Plants": Plants})


def contact_view (request:HttpRequest):
    if request.method == "POST":
        new_data = Contact(first_name=request.POST["first_name"], last_name=request.POST["last_name"],email=request.POST["email"], message=request.POST["message"],created_at = True) 
        new_data.save()
    return render(request,'main/contact.html')



def contact_messages(request:HttpRequest):
    data = Contact.objects.all()

    return render (request , 'main/contacUsMessages.html' , {'data':data})
