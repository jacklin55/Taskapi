from http.client import REQUEST_ENTITY_TOO_LARGE, responses
import json
from telnetlib import STATUS
from typing import Generic
from urllib import request, response
from urllib.parse import urlsplit
from rest_framework.response import Response
from rest_framework import generics
import requests
from .models import CurrencyModel
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .Serializer import CurrencySerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.parsers import JSONParser



@api_view(('GET',))
def get_queryset(self):
        data = self.request.data
        list_of_cat = data['amount']  
        qs = CurrencyModel.objects.filter(amounty__icontains=list_of_cat)
        return HttpResponse(qs) 


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@permission_classes((permissions.AllowAny,))
def call_api(request, format=None):
    url = "https://api.frankfurter.app/latest?to=USD,GBP"
    
    header = {}
    # CurrencyModel.objects.all().delete()
    result = requests.get(url,headers=header)
    dat = result.content
    my_json = dat.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    s = json.dumps(data, indent=4, sort_keys=True)
    # print(data.items())
    for key, value in data.items():
        if key == "amount":
            x=value
        if key == "base":
             y= value
        if key == "date":
            dd=value
        if key == "rates":
            for x , y in value.items():
                createcurrency = CurrencyModel.objects.create(tocurrency = x,rate = y,
                amount=x,fromcurrency=y,Data_currency=dd)
    return HttpResponse(result.content)
