from django.db import models
from accounts.models import Profile, Applicant

class Job(models.Model):

    recruiter = models.ForeignKey('accounts.Profile', on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    pay = models.IntegerField()
    last_date = models.DateField()

class Application(models.Model):

    job = models.ForeignKey('Job', on_delete = models.CASCADE)
    applicant = models.ForeignKey('accounts.Applicant', on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)