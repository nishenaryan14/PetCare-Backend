# serializers.py
from rest_framework import serializers
from .models import User, Pet, UserProfile


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, max_length=128)

    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PetSerializer(serializers.Serializer):
    pet_id = serializers.IntegerField()
    animal = serializers.ChoiceField(choices=Pet.ANIMAL_CHOICES)
    breed = serializers.CharField(max_length=50)
    climate = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Pet(**validated_data)


class UserProfileSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    favorite_pets = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all()))

    def create(self, validated_data):
        return UserProfile(**validated_data)
