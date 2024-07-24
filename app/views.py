from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, UserProfile, Pet
from .serializers import UserSerializer, PetSerializer, UserProfileSerializer
from mongoengine import DoesNotExist
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


def create_pet(pet_data):
    serializer = PetSerializer(data=pet_data)
    if serializer.is_valid():
        pet = serializer.save()
        print(pet)
        return pet
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddFavoritePetView(APIView):
    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        pet_id = request.data.get('pet_id')
        if not pet_id:
            return Response({'error': 'Missing pet_id in request data'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            pet = Pet.objects.get(pk=pet_id)  # Use MongoEngine's get with pk
        except DoesNotExist:
            pet_data = request.data.copy()  # Avoid modifying original request data
            serializer = PetSerializer(data=pet_data)
            if serializer.is_valid():
                pet = serializer.save()  # Save the pet first
                print(pet_data)
                print(serializer.data)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            profile = UserProfile.objects.get(user=user)
        except DoesNotExist:
            profile = UserProfile(user=user)

        # if not isinstance(pet, Pet):
        #     return pet

        profile.favorite_pets.append(pet)
        profile.save()
        return Response({"message": "Pet added to favorites"}, status=status.HTTP_200_OK)

    #TODO: pet info not getting stored in pet collection


class RemoveFavoritePetView(APIView):
    pass


class GetFavoritePetsView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            user_profile = UserProfile.objects.get(user=user)
        except DoesNotExist:
            return Response({"error": "User profile not found"}, status=status.HTTP_404_NOT_FOUND)

        pets = user_profile.favorite_pets

        print(pets)

        # Serialize the list of favorite pets
        pet_list = PetSerializer(pets, many=True).data

        return Response(pet_list, status=status.HTTP_200_OK)

