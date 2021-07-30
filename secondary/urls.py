from django.urls import path
from . import views

urlpatterns = [
    path('', views.getroutes, name='routes'),
    path('contact/create/', views.createContact, name='createcontact'),
]
