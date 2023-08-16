from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def create_quote(request):
    return render(request, 'create_quote.html')

def create_invoice(request):
    return render(request, 'create_invoice.html')