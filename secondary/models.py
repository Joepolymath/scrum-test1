from django.db import models

# Create your models here.

class ContactUs(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=1000)
    date_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Contacts'

    def __str__(self):
        return self.email
