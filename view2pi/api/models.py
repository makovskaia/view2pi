  
from django.db import models
from django.forms import ModelForm
# Create your models here.

class Image(models.Model):
    url = models.URLField(max_length=200)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.description

class Marker(models.Model):
    image_from = models.ForeignKey(Image,related_name='image_from', on_delete=models.CASCADE)
    image_to = models.ForeignKey(Image,related_name='image_to', on_delete=models.CASCADE)
    lat = models.CharField(max_length=100, default='0deg')
    lng = models.CharField(max_length=100, default='0deg')
    

# class User(models.Model):
#     email=models.EmailField()
#     name=models.CharField(max_length=20)
#     phone=models.IntegerField()

# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'email', 'phone']