from rest_framework import serializers
from .models import EmployeeProfile, EmployerProfile

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = ['id', 'user', 'resume', 'skill1', 'skill2', 'skill3', 'bio', 'experience', 'country', 'picture','phone']
        read_only_fields = ['id', 'user']
class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ['id', 'user', 'company_logo', 'location', 'bio', 'contact_phone']
        read_only_fields = ['id', 'user']