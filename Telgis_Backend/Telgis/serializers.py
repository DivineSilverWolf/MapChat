from rest_framework import serializers

from Telgis.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['login']
