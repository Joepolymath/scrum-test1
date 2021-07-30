from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactUs
from .serializers import ContactSerializer

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

@api_view(['GET'])
def retrieveContacts(request):
    contacts = ContactUs.objects.all()
    serializer = ContactSerializer(contacts, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def retrieveContact(request, pk):
    contact = ContactUs.objects.get(id=pk)
    serializer = ContactSerializer(contact, many = False)
    return Response(serializer.data)
