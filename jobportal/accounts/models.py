from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    MALE = 'MA'
    FEMALE = 'FE'
    OTHER = 'OT'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 40)
    occupation = models.CharField(max_length = 40)
    company_name = models.CharField(max_length = 50)
    is_recruiter = models.BooleanField(default=False) 
    gender = models.CharField(
        max_length = 2,
        choices = GENDERS,
        default = MALE
        )

class Applicant(models.Model):

    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    # organization = models.CharField(max_length = 50)
    is_student = models.BooleanField(default=False)
    experience = models.IntegerField()
    description = models.TextField(null = True)
    skills = models.TextField(null=True)
    education = models.TextField()
    certification = models.TextField(null = True)

#education and certifications can have their wn models but I
# didn't want to make the code very long, though I considered it in my list of models 