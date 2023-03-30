from django.contrib import admin

# Register your models here.
from .models import Site, Account
admin.site.register(Site)
admin.site.register(Account)