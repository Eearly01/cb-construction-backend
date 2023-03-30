from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import SiteSerializer, RegistrationSerializer, AccountPropertiesSerializer
from .models import Site, Account

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

def csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

@api_view(['POST',])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET',])
@permission_classes((IsAuthenticated))
def account_properites_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AccountPropertiesSerializer(account)
    Response(serializer.data)


@api_view(['GET',])
@permission_classes((IsAuthenticated))
def update_account_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AccountPropertiesSerializer(account, data=request.data)
    data ={}
    if serializer.is_valid():
        serializer.save()
        data['response'] = "Account update success"
        return Response(data=data)
    Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
