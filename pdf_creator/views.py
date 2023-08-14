# from django.shortcuts import render
import pdfkit
import jinja2
from datetime import datetime

# Create a pdf variables
date = datetime.today().strftime("%d - %b - %y")
client = "Empresas Juanito"
number = 1
first_product = "Pc gamer"
fp_cant = 3
fp_price = 234
second_product = "Liquido de frenos"
sp_cant = 19
sp_price = 15
sub_total = fp_cant * fp_price + sp_cant * sp_price
taxes = sub_total * 0.10
total = sub_total + taxes

# The diccionary about the variables for insert in html
context = {
    "date": date,
    "client": client,
    "number": number,
    "first_product": first_product,
    "fp_cant": fp_cant,
    "fp_price": fp_price,
    "second_product": second_product,
    "sp_cant": sp_cant,
    "sp_price": sp_price,
    "sub_total": sub_total,
    "taxes": taxes,
    "total": total
}

# Templates configuration
template_loader = jinja2.FileSystemLoader("pdf_creator/templates/")
template_env = jinja2.Environment(loader=template_loader)
html_template = 'quote.html'
template = template_env.get_template(html_template)

config_pdf = pdfkit.configuration(wkhtmltopdf="pdf_creator/wkhtmltopdf/bin/wkhtmltopdf.exe")

# Output (name, path) configuration
output_text = template.render(context)
output_pdf_path = 'pdf/'
output_pdf_filename = 'quote_' + str(number) + '.pdf'
output_pdf = output_pdf_path + output_pdf_filename

pdfkit.from_string(output_text, output_pdf, configuration=config_pdf)