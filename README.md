# Taskapi
actived env :
tack_env\Scripts\activate.bat
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
this is to run server 
http://127.0.0.1:8000/taskapi this is to call api and sord local data and return data
http://127.0.0.1:8000/CurrencyApi/latest?to=USD,GBP
(OR)
Send Get request using python:

import requests

session = requests.Session()

products = session.get("http://127.0.0.1:8000/api/generate_view_product/", json={"amount":1})

print(products.text)




