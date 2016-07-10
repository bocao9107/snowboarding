from django.shortcuts import render,render_to_response
import datetime
from django.http import HttpResponse
from .models import Product
from django.contrib import messages
from django.template import RequestContext,loader

# Create your views here.
def sellmainpage(request):
    template=loader.get_template("templates/sell.html")
    products=Product.objects.all()
    context= RequestContext(request,{
    'products':"products"}
    )
    return HttpResponse(template.render(context))

def detail (request):
    return render(request,'sell/item_detail.html',)
