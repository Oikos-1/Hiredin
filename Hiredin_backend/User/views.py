from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import EmployerProfile,EmployeeProfile
from .serializers import EmployeeSerializer, EmployerSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_profile(request):
    if request.user.role == "Employee":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.user.role == "Employer":
        serializer = EmployerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"error": "User role is not recognized."}, status=status.HTTP_400_BAD_REQUEST)