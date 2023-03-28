from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import SiteSerializer
from .models import Site
# Create your views here.

class MyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# INDEX, CREATE
class SiteList(generics.ListCreateAPIView):
    queryset = Site.objects.all().order_by('id')
    serializer_class = SiteSerializer

# SHOW, PUT, DELETE
class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all().order_by('id')
    serializer_class = SiteSerializer