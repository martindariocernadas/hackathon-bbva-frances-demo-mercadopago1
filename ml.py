# Import Mercadopago library
import os, sys
import mercadopago

import json

# Create an instance with your MercadoPago credentials (CLIENT_ID and CLIENT_SECRET): 
# Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
# Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes
mp = mercadopago.MP("5643352584449553", "kM7TSzfwksQPaUBi22VVEa3P97D2kXNW")

filters = {
        "site_id": "MLA", # Argentina: MLA; Brasil: MLB
        "external_reference": "Bill001"
    }

# Search payment data according to filters
searchResult = mp.search_payment(filters)

# Show payment information
output = "" 

for payment in searchResult["response"]["results"]:
        output += "<tr>"
        output += "<td>"+payment["collection"]["id"]+"</td>\n"
        output += "<td>"+payment["collection"]["external_reference"]+"</td>\n"
        output += "<td>"+payment["collection"]["status"]+"</td>\n"
        output += "</tr>"
    	output += " "

print output
print "Ok!"
