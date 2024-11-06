from django.db import models
from authentication.models import CustomUser

class EmployeeProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="employee_profile")
    resume = models.URLField(max_length=500, null=True, blank=True)
    skill1 = models.CharField(max_length=50, null=True, blank=True)
    skill2 = models.CharField(max_length=50, null=True, blank=True)
    skill3 = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    experience = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="employer_profile")
    company_name = models.CharField(max_length=255)
    company_logo = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    contact_phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.company_name
