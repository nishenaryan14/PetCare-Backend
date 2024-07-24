# serializers.py
from rest_framework import serializers
from .models import User, Pet, UserProfile


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, max_length=128)
    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email')

    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PetSerializer(serializers.Serializer):
    # pet_id = serializers.IntegerField()
    animal = serializers.CharField(max_length=50)
    breed = serializers.CharField(max_length=50)
    climate = serializers.CharField(max_length=50)

    def create(self, validated_data):
        pet = Pet(**validated_data)
        # pet = Pet(pet_id=151, animal="dog", breed="Labrador", climate="Temperate")
        # print(Pet._get_collection().index_information())

        pet.save()
        return pet

        # if pet.pet_id is None:
        #     raise serializers.ValidationError("pet_id cannot be null")
        #
        # try:
        #     pet = Pet(pet_id=150, animal= validated_data['animal'], breed= validated_data['breed'],
        #               climate= validated_data['climate'])
        #     pet.save()
        #     print("Pet saved successfully")
        # except Exception as e:
        #     print(f"Error saving pet: {str(e)}")
        # raise


class UserProfileSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    favorite_pets = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all()))

    def create(self, validated_data):
        return UserProfile(**validated_data)
