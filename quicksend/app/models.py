from django.db import models

class Email(models.Model):
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=60)
# Create your models here.
