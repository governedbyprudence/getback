from django.db import models
# Create your models here.

class users(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    creation=models.DateTimeField(auto_now_add=True)
