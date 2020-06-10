# get_data.py
print("REQUESTING SOME DATA FROM THE INTERNET...")

import json
import requests

request_url= "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
print(response.status_code)
print(response.text)
print(type(response.text))

product = json.loads(response.text)

print(type(product)) #> <class 'dict'>

##print(product) #> {'first_name': 'Ophelia', 'last_name': 'Clarke', 'message': 'Hi, thanks for the ice cream!', 'fav_flavors': ['Vanilla Bean', 'Mocha', 'Strawberry']}
print(product["name"])
##print(parsed_response["name"])



breakpoint()

request_url= "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response = requests.get(request_url)
print(response.status_code)
print(response.text)
print(type(response.text))

product = json.loads(response.text)
