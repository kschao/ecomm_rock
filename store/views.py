from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request, "store/index.html")

def collections(request):
    category = Product.objects.filter(id=0)
    context = { 'products': Product}
    return render(request, "store/collections.html", context)