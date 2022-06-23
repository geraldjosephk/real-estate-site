from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=100, unique=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

