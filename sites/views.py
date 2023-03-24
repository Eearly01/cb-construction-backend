from rest_framework import generics
from .serializers import SiteSerializer
from .models import Site
# Create your views here.

# INDEX, CREATE
class SiteList(generics.ListCreateAPIView):
    queryset = Site.objects.all().order_by('id')
    serializer_class = SiteSerializer

# SHOW, PUT, DELETE
class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all().order_by('id')
    serializer_class = SiteSerializer