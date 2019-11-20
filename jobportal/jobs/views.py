import datetime
from django.shortcuts import render, redirect
from django import views
from django.urls import reverse
from accounts.models import Profile, Applicant
from .models import Job, Application
from .forms import JobForm

class JobView(views.View):

    def post(self, request):

        user = request.user
        person = user.profile

        if person.is_recruiter is True:
            
            form = JobForm(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.recruiter = person
                obj.save()

                return redirect(reverse('jobs:posted_jobs'))

            return render(request,reverse('jobs:post_job'),{'success':False})
        
    def get(self, request):

        form = JobForm()

        return render(request,'post_job.html',{'form':form, 'success': True})

class JobDetails(views.View):

    def get(self, request, id):

        try:
            job = Job.objects.get(id = id)
        except Job.DoesNotExist:
            return redirect(reverse('accounts:dashboard'))

        return render(request, 'job_details.html', {'job':job})
        

class PostedJobs(views.View):
    
    def get(self, request):

        user = request.user
        person = user.profile

        if person.is_recruiter is True:
            
            jobs = Job.objects.filter(recruiter = person)

            return render(request,'posted_jobs.html',{'jobs':jobs})
        
        else:

            return redirect('/')

class AllJobs(views.View):
    
    def get(self, request):

        current_date = datetime.datetime.now()

        all_jobs = Job.objects.filter(last_date__gte = current_date)

        return render(request, 'all_jobs.html', {'jobs':all_jobs})

class AllApplicationsForJob(views.View):
    
    def get(self, request, id):

        job = Job.objects.get(id = id)

        applications = Application.objects.filter(job = job)

        return render(request, 'applications.html', {'applications': applications})
        

class ApplicationView(views.View):
    
    def get(self, request, id):

        user = request.user
        try:
            person = user.profile
        except Profile.DoesNotExist:
            return redirect(reverse('accounts:details'))

        if person.is_recruiter is False:

            print(person)

            try:
                applicant = Applicant.objects.get(user=person)
            except Applicant.DoesNotExist:
                return redirect(reverse('accounts:applicant')) 

            try:
                job = Job.objects.get(id = id)
            except Job.DoesNotExist:
                return redirect('') #redirect to all jobs

            application = Application.objects.create(applicant = applicant, job = job)
            
            application.save()

            return redirect(reverse('jobs:applied_jobs'))
        
        else:

            return redirect(reverse('accounts:dashboard'))

class ApplicantAllApplications(views.View):
    
    def get(self, request):

        user = request.user
        
        try:
            person = user.profile
        except Profile.DoesNotExist:
            return redirect(reverse('accounts:details'))

        if person.is_recruiter is False:

            try:
                applicant = Applicant.objects.get(user=person)
            except Applicant.DoesNotExist:
                return redirect(reverse('accounts:applicant'))

            applications = Application.objects.filter(applicant = applicant)

            return render(request,'applied_jobs.html',{'applications':applications})
        
        else:

            return redirect('/')

        
