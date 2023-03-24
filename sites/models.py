from django.db import models

# Create your models here.
class Site(models.Model):
    job = models.CharField(max_length=32)
    footage = models.IntegerField()
    def __str__(self): return str(self.job)