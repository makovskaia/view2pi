from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    phone=models.IntegerField()
    ip = models.GenericIPAddressField()
