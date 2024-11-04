from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . serialiazers import RegisterSerializer, LoginSerializer
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='post', request_body=RegisterSerializer, responses={201: 'User registered successfully!', 400: 'Validation error'})
@api_view(['POST'])
def register(request):
    data = JSONParser().parse(request)
    serializer = RegisterSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "User registered successfully!"}, status=201)
    
    return JsonResponse(serializer.errors, status=400)


@swagger_auto_schema(method='post', request_body=LoginSerializer, responses={200: 'Login successful', 400: 'Validation error'})
@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        return JsonResponse({"message": "Login successful"}, status=200)
    
    return JsonResponse(serializer.errors, status=400)
