from rest_framework import serializers

from Telgis.models import Users, Locations

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['login']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ['login', 'latitude', 'longitude', 'timestamp']