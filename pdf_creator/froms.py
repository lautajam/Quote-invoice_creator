from django.forms import ModelForm
from .models import Product, Client

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "important"]

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["title", "description", "important"]