from django.http import JsonResponse
from .serialiazers import RegisterSerializer, LoginSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate
from .serialiazers import CustomTokenObtainPairSerializer

@swagger_auto_schema(
    method='post',
    request_body=RegisterSerializer,
    responses={201: 'User registered successfully!', 400: 'Validation error'}
)
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "User registered successfully!"}, status=201)
    return JsonResponse(serializer.errors, status=400)


@swagger_auto_schema(
    method='post',
    request_body=LoginSerializer,
    responses={200: 'Login successful', 400: 'Validation error'}
)
@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            token_serializer = CustomTokenObtainPairSerializer(data={
                'username': username,
                'password': password
            })
            if token_serializer.is_valid():
                tokens = token_serializer.validated_data
                return JsonResponse({
                    "message": "Login successful",
                    "access": tokens['access'],
                    "refresh": tokens['refresh']
                }, status=200)
            return JsonResponse({"error": "Could not generate token"}, status=400)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)
    
    return JsonResponse(serializer.errors, status=400)
