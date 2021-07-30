from django.db import models

# Create your models here.

class ContactUs(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=1000)
    phone = models.CharField(max_length=20, default='nil')
    address = models.CharField(max_length=200, default='nil')
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
