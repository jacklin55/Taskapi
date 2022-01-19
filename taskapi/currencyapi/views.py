from http.client import REQUEST_ENTITY_TOO_LARGE, responses
import json
from telnetlib import STATUS
from typing import Generic
from urllib import request, response
from urllib.parse import urlsplit
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
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

    # serializer = CurrencySerializer(result.content, many= True)
    # return response(serializer.content)

        # if key == "amount":
        #     print(1,value)
        #     createcurrency = CurrencyModel.objects.create(  
        #               amount=value
        #               )
        # if key == "base":
        #     print(2,value)
        #     createcurrency = CurrencyModel.objects.create(
        #               fromcurrency=value
        #               )
        # if key == "date":
        #     print(3,value)
        #     createcurrency = CurrencyModel.objects.create(
        #               Data_currency=value
        #               )
        # if key == "rates":
        #     for x , y in value.items():

        #         print(x)
        #         print ("////////////")
        #         createcurrency = CurrencyModel.objects.create(tocurrency = x,rate = y
                    
                      
                  
                # createcurrency = CurrencyModel.objects.create(
                #       rate = y
                #       )
    # return HttpResponse(result.content)








    # serializer = CurrencySerializer(currdata, many= True)
    # return response(serializer.data)
    # print (2,result.data)
    # # payload = {'amount':'My_Secret_Token','base':request.POST.get("base"),'rates':request.POST.get("rates")}
    # # r = requests.post(url, data = payload)
    # if result.status_code == 200:
    #     data = result.text
    #     return Response(data, status=STATUS.HTTP_200_OK)
    # return HttpResponse('Something went wrong')


    # rs = (grequests.get('https://api.frankfurter.app/latest?amount=9&from=GBP&to=EUR'))
    # print ("//////////////////////////   ",rs )
    # blah = grequests.map(rs)
    # print (blah[0].json())



























#9 create new reservation 
# @api_view(['POST'])
# def new_reservation(request):

#     movie = Movie.objects.get(
#         hall = request.data['hall'],
#         movie = request.data['movie'],
#     )
#     guest = Guest()
#     guest.name = request.data['name']
#     guest.mobile = request.data['mobile']
#     guest.save()

#     reservation = Reservation()
#     reservation.guest = guest
#     reservation.movie = movie
#     reservation.save()

#     return Response(status=status.HTTP_201_CREATED)








# class Currency(models.Model):
    # def home(request):
    #     client = coreapi.Client()
    #     data = client.get('http://127.0.0.1:8000/api/usersapi/1/')

    #     name = data.get("name")
    #     age = data.get("age")
    #     gender = data.get("gender")
    #     user = UserData.objects.create(name=name, age=age, gender=gender)
    #     user.save()

    #     return HttpResponse(f"OKAY, got and saved user {name}").
