from django.db import models

# Create your models here.
class JobCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class JobPost(models.Model):

    FULL_TIME = 'Full-time'
    PART_TIME = 'Part-time'
    CONTRACT = 'Contract'
    INTERN = 'Internship'
    FREELANCE = 'Freelance'
    EMPLOYMENT_TYPE = [
        (FULL_TIME, 'Full-time'),
        (PART_TIME, 'Part-time'),
        (CONTRACT, 'Contract'),
        (INTERN, 'Internship'),
        (FREELANCE, 'Freelance'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE)
    created_time = models.DateTimeField(auto_now_add=True)
    #employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name="job_posts")
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, related_name="job_posts")

    def __str__(self):
        return f"{self.title} at {self.company}"