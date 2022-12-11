from django.db import models

# Create your models here.


class logform(models.Model):
    name = models.CharField(max_length=44)
    email = models.EmailField(max_length=44)
    phone = models.CharField(max_length=44)
