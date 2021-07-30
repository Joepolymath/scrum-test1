from rest_framework import serializers
from .models import ContactUs

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

