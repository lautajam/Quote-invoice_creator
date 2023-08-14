from django.db import models

# Create your models here.
class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Amount: {self.amount}, Price: {self.price}"

class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"