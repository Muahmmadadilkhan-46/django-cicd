# Rest Framework Imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, NotFound

# Local Imports
from core.models import DoctorProfile, PatientProfile
from core.serializers import DoctorProfileSerializer, PatientProfileSerializer
from core.authentication import JWTAuthentication

# Django Imports
from django.shortcuts import get_object_or_404


class ProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get the user profile
        """
        user = request.user

        DoctorProfile.objects.filter(user=user).exists()

        if not user:
            raise NotFound("User not found.")

        if user.role == "doctor":
            # Check if the user has a doctor profile otherwise raise a 404
            if not DoctorProfile.objects.filter(user=user).exists():
                raise NotFound("Profile not found.")

            profile = DoctorProfile.objects.get(user=user)
            serializer = DoctorProfileSerializer(profile)

        elif user.role == "patient":
            # Check if the user has a patient profile otherwise raise a 404
            if not PatientProfile.objects.filter(user=user).exists():
                raise NotFound("Profile not found.")

            profile = PatientProfile.objects.get(user=user)
            serializer = PatientProfileSerializer(profile)

        else:
            # Check if the user is an admin otherwise raise a 403
            raise PermissionDenied("Not allowed.")

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create the user profile
        """
        user = request.user
        data = request.data.copy()
        data["user"] = user.id

        if user.role == "doctor":
            serializer = DoctorProfileSerializer(data=data)
        elif user.role == "patient":
            serializer = PatientProfileSerializer(data=data)
        else:
            # Check if the user is an admin otherwise raise a 403
            raise PermissionDenied("Not allowed.")

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        """
        Update the user profile
        """
        user = request.user

        if user.role == "doctor":
            profile = get_object_or_404(DoctorProfile, user=user)
            serializer = DoctorProfileSerializer(
                profile, data=request.data, partial=True
            )
        elif user.role == "patient":
            profile = get_object_or_404(PatientProfile, user=user)
            serializer = PatientProfileSerializer(
                profile, data=request.data, partial=True
            )
        else:
            # Check if the user is an admin otherwise raise a 403
            raise PermissionDenied("Not allowed.")

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        """
        Delete the user profile
        """
        user = request.user

        if user.role == "doctor":
            profile = DoctorProfile.objects.get(user=user)
        elif user.role == "patient":
            profile = PatientProfile.objects.get(user=user)
        else:
            # Check if the user is an admin otherwise raise a 403
            raise PermissionDenied("Not allowed.")

        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
