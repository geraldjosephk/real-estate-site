from email import message
from unicodedata import name
from django.db import models

class Contact(models.Model):
    listing = models.CharField(max_length=100)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField(max_length=200)
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.name