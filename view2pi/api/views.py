from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django import forms
from django.forms import modelform_factory
from django.template import Context
from django.template.loader import get_template
from api.models import Image, Marker
from django.views.decorators.http import require_http_methods
from django.core import serializers
# @require_http_methods(["POST"])
# def index(request):
#     # f=UserForm(request.POST)
#     if f.is_valid():
#         name = f.cleaned_data['name']
#         email = f.cleaned_data['email']
#         phone = f.cleaned_data['phone']
#         u = User(name=name, email=email,phone=phone)
#         u.save()
#         return HttpResponse(u.id)
#     return HttpResponse('no')


@require_http_methods(["GET"])
def image(request, id):
    try:
        markers = Marker.objects.filter(image_from_id=id)
        response = JsonResponse({
            'markers': [{'id': m.image_to.id, 'lat': m.lat, 'lng': m.lng} for m in markers],
            'image': markers[0].image_from.url
        })
        print(response)

    finally:
        print('lol')
        res = 'lol'
    return response

    # f=UserForm(request.POST)
    # if f.is_valid():
    #     name = f.cleaned_data['name']
    #     email = f.cleaned_data['email']
    #     phone = f.cleaned_data['phone']
    #     u = User(name=name, email=email,phone=phone)
    #     u.save()
    #     return HttpResponse(u.id)
    # return HttpResponse('no')






