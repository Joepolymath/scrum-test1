from django.urls import path
from . import views

urlpatterns = [
    path('', views.getroutes, name = 'routes'),
    path('contact/retrieve/', views.retrieveContacts, name ='retrieve'),
    path('contact/<str:pk>/retrieve/', views.retrieveContact, name = 'retrieve'),
]