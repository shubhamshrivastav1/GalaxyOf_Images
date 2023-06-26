from django.http import HttpRequest
from django.shortcuts import redirect, render
from myapp.models import *


def show_home_page(request):

    cats=Category.objects.all()
    images=Image.objects.all() 
    data={'images':images,'cats':cats}
    return render(request,"home.html", data)


def show_category_page(request,cid):
    print(cid)

    cats=Category.objects.all()
    images=Image.objects.all() 



    category=Category.objects.get(pk=cid)
    print(category)

    images=Image.objects.filter(cat=category)


    data={'images':images,'cats':cats}
    return render(request,"home.html", data)


def home(request):
    return redirect('/home')