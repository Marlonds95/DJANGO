from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def product(request):
    return render(request,'core/product.html')
def contact(request):
    return render(request,'core/contact.html')