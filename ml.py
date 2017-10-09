# Import Mercadopago library
import os, sys
import mercadopago

import json

# Create an instance with your MercadoPago credentials (CLIENT_ID and CLIENT_SECRET): 
# Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
# Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes
mp = mercadopago.MP("...", "...")

filters = {
        "site_id": "MLA", # Argentina: MLA; Brasil: MLB
    }


# Search payment data according to filters
searchResult = mp.search_payment(filters)

# Show payment information
output = "" 

for payment in searchResult["response"]["results"]:
   output += "<tr>"
   output += "<td>"+payment["collection"]["id"]+"</td>\n"
   payment_id = payment["collection"]["id"]
   output += "<td>"+payment["collection"]["external_reference"]+"</td>\n"
   output += "<td>"+payment["collection"]["status"]+"</td>\n"
   output += "</tr>"
   output += " "

   paymentInfo = mp.get_payment (payment_id)
   if paymentInfo["status"] == 200:
     print json.dumps(paymentInfo, indent=4)
     print "Ok..."
   else:
     print "None!"


print "Ok!"
