from django.shortcuts import render

# Create your views here.

def pdf_create(request):
    return render(request, "pdf_create.html")