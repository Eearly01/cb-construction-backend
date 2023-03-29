from rest_framework import serializers
from .models import Site, User

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('id', 'job', 'footage')

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')