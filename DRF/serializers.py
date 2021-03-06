from django.contrib.auth import authenticate
from rest_framework import serializers
from account.models import User
#from donation.models import Donated, DonationItem
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.CharField()

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return User.objects.create(**validated_data)



class UserDisplaySerializer(serializers.Serializer):
    id = serializers.CharField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return User.objects.create(**validated_data)



"""         REGISTERATION STARS HERE        """
class UserRegisterSerializer1(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'],
                                        last_name=validated_data['last_name'], first_name=validated_data['first_name'])

        return user

