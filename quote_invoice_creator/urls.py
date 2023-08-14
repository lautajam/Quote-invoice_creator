"""
URL configuration for quote_invoice_creator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front_logic import views as views_front
# from email_send import views as views_email
# from pdf_creator import views as views_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_front.home, name="home"),
    # path('email_send/', views_email.email_send, name="email_send"),
    # path('pdf_create/', views_pdf.pdf_create, name="pdf_creator"),
]
