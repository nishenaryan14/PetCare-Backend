from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import User, UserProfile, Pet
from .serializers import UserSerializer, PetSerializer, UserProfileSerializer
from mongoengine import DoesNotExist


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
                return Response({"message": "Login successful", "user_id": str(user.id)}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class AddFavoritePetView(APIView):
    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            pet = Pet.objects.get(id=request.data.get('pet_id'))
        except DoesNotExist:
            return Response({"error": "Pet not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            profile = UserProfile.objects.get(user=user)
        except DoesNotExist:
            profile = UserProfile(user=user)

        profile.favorite_pet.append(pet)
        profile.save()
        return Response({"message": "Pet added to favorites"}, status=status.HTTP_200_OK)

