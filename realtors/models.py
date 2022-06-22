from django.db import models

class Realtor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=100, unique=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.realtor_name

