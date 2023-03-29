from django.db import models

# Create your models here.
class Site(models.Model):
    job = models.CharField(max_length=32)
    footage = models.IntegerField()
    def __str__(self): self.job

class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    def  __str__(self):
        return self.username
    