from django.shortcuts import render

# Create your views here.

def email_send(request):
    return render(request, "email_send.html")