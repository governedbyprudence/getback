from django.db import models
# Create your models here.

class users(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    token=models.UUIDField(null=True)
    creation=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username