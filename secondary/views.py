from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

@api_view(['GET'])
def getroutes(request):
    routes = [
        {
            'endpoint': '/contact/create',
            'method': 'POST',
            'description': 'posts or sends the contact us form content',
        },
        {
            'endpoint': '/contact/id/update/',
            'method': 'PUT',
            'description': 'updates the data'
        },
        {
            'endpoint': '/contact/id/delete/',
            'method': 'DELETE',
            'description': 'deletes the data'
        },
        {
            'endpoint': '/contact/retrieve/',
            'method': 'GET',
            'description': 'deletes the data'
        },
        {
            'endpoint': '/contact/id/retrieve/',
            'method': 'GET',
            'description': 'deletes the data'
        },
    ]
    
    return Response(routes)


@api_view(['POST'])
def createContact(request):
    data = request.data
    contact = ContactUs.objects.create(first_name = data['first_name'], last_name = data['last_name'], email = data['email'], message = data['message'], phone = data['phone'], address = data['address'])
    serializer = ContactSerializer(contact, many=False)
    return Response(serializer.data)
