from django.shortcuts import render

def home(request):
    return render(request, 'burgir/home.html')

def menu(request):
    return render(request, 'burgir/menu.html')