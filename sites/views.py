from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SiteSerializer, UserSerializer
from .models import Site, User
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

def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)