# from django.shortcuts import render
import pdfkit
import jinja2
from datetime import datetime
from models import Client, Product

# Clculates a subtotal, teaxes and total about the products
def calculator_total(products, taxes_porcent):
    subtotal, taxes, total = 0, 0, 0
    for product in products:
        subtotal += product.amount * product.price
    taxes = subtotal * (taxes_porcent / 100)
    total = subtotal + taxes
    return subtotal, taxes, total

# Templates configuration
template_loader = jinja2.FileSystemLoader("pdf_creator/templates/")
template_env = jinja2.Environment(loader=template_loader)
html_template = 'invoice.html'
template = template_env.get_template(html_template)

# PDF config
config_pdf = pdfkit.configuration(wkhtmltopdf="pdf_creator/wkhtmltopdf/bin/wkhtmltopdf.exe")

# Create a pdf variables
date = datetime.today().strftime("%d - %b - %y")

taxes_porcent = (int(input('Type taxes (in %, just the number): ')))

products = [
    Product("Gas", 13, 100),
    Product("Paper", 5, 345),
    Product("Sponge", 1, 10)
]

subtotal, taxes, total = calculator_total(products, taxes_porcent)

client = Client("Empesa Juanito", "juancitoenterprice@gmail.com")

purchase_number = 1

# The diccionary about the variables for insert in html
context = {
    'date': date,
    'purchase_number': purchase_number,
    'client': client,
    'products': products,
    'subtotal': subtotal,
    'taxes': taxes,
    'taxes_porcent': taxes_porcent,
    'total': total
}

# Output (name, path) configuration
output_text = template.render(context)
output_pdf_path = 'pdf/'
output_pdf_filename = 'invoice_' + str(purchase_number) + '.pdf'
output_pdf = output_pdf_path + output_pdf_filename

pdfkit.from_string(output_text, output_pdf, configuration=config_pdf)