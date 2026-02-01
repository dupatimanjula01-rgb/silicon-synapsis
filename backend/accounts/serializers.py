from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['is_admin', 'cgpa', 'department']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    cgpa = serializers.FloatField(required=False, write_only=True)
    department = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'cgpa', 'department']

    def create(self, validated_data):
        cgpa = validated_data.pop('cgpa', None)
        department = validated_data.pop('department', '')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Update profile
        user.profile.cgpa = cgpa
        user.profile.department = department
        user.profile.save()
        return user
