from django.urls import path
from .views import *

urlpatterns = [
    path('profile/employee', CreateEmployeeProfile.as_view(), name='create_profile'),
    path('profile/employer', CreateEmployerProfile.as_view(), name='create_profile'),
    path('profile/employee/setting', EmployeeprofileRUD.as_view(), name='employee-profile'),
    path('profile/employer/setting', EmployerprofileRUD.as_view(), name='employer-profile'),
]