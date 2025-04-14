from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    organization = serializers.CharField(default="Default Organization")
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICES, default='user')

    class Meta:
        model = Profile
        fields = ['user', 'organization', 'role', 'created_at']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    organization = serializers.CharField(write_only=True, required=False)
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICES, write_only=True, required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'organization', 'role']

    def create(self, validated_data):
        organization = validated_data.pop('organization', 'Default Organization')
        role = validated_data.pop('role', 'user')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Profile.objects.create(
            user=user,
            organization=organization,
            role=role
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['role'] = user.profile.role
        return token