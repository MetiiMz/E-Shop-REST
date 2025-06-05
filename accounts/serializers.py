from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'full_name', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    # Remove password2 and create a new user using the create_user method from UserManager
    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)

    # Check that password and password2 match
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('The password must be the same')
        return data


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
