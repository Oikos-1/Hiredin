from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import EmployeeSerializer, EmployerSerializer
from authentication.permissions import IsEmployee, IsEmployer
from .models import *

class CreateEmployeeProfile(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,IsEmployee]
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        if EmployeeProfile.objects.filter(user=self.request.user).exists():
            return Response({"error": "You have already created"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateEmployerProfile(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,IsEmployer]
    serializer_class = EmployerSerializer

    def create(self, request, *args, **kwargs):
        if EmployerProfile.objects.filter(user=self.request.user).exists():
            return Response({"error": "You have already created"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeprofileRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsEmployee]
    serializer_class = EmployeeSerializer
    queryset = EmployeeProfile.objects.all()

    def get_object(self):
        return self.get_queryset().filter(user=self.request.user).first()
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class EmployerprofileRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsEmployer]
    serializer_class = EmployerSerializer
    queryset = EmployerProfile.objects.all()

    def get_object(self):
        return self.get_queryset().filter(user=self.request.user).first()
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
