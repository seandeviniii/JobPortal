from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django import views
from .forms import ProfileForm, ApplicantForm
from .models import Profile

def signup(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('accounts:details'))
    else:
        if request.user.is_authenticated:
            return redirect(reverse("accounts:dashboard"))
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class GetHome(views.View):

    def get(self, request):

        if request.user.is_authenticated:
            return redirect(reverse("accounts:dashboard"))
            
        return render(request, 'home.html')

class GetDashboard(views.View):

    def get(self, request):

        user = request.user

        try:
            person = user.profile
        except Profile.DoesNotExist:
            return redirect(reverse('accounts:details'))

        return render(request, 'dashboard.html', {'person':person})

class RegisterView(views.View):

    def post(self, request):

        user = request.user

        try:

            person = user.profile

        except Profile.DoesNotExist:    

            form = ProfileForm(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = user
                obj.save()
        
                return redirect(reverse('accounts:dashboard'))

        name = request.POST.get('name')
        occupation = request.POST.get('occupation')
        company_name = request.POST.get('company_name')
        is_recruiter = True if (request.POST.get('is_recruiter') == 'on') else False
        gender = request.POST.get('gender')

        person = Profile.objects.filter(user=user).update(
            name = name,
            occupation = occupation,
            company_name = company_name,
            is_recruiter = is_recruiter,
            gender = gender
        )
        # person.save()

        return redirect(reverse('accounts:dashboard'))

        
    def get(self, request):

        # user = request.user
        # profile = Profile.objects.create(user = user)
        # form = ProfileForm(instance = profile, data = request.POST)
        form = ProfileForm()

        return render(request,'profile.html',{'form':form})

class ApplicantView(views.View):

    def post(self, request):

        user = request.user
        
        try:
            person = user.profile
        except Profile.DoesNotExist:
            return redirect(reverse('accounts:details'))

        print(person)

        form = ApplicantForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = person
            obj.save()

            return redirect(reverse('accounts:dashboard'))

        is_student = request.POST.get('is_student')
        experience = request.POST.get('experience')
        description = request.POST.get('description')
        skills = True if (request.POST.get('skills') == 'on') else False
        education = request.POST.get('education')
        certification = request.POST.get('certification')

        applicant = Applicant.objects.filter(user=person).update(
            is_student = is_student,
            experience = experience,
            description = description,
            skills = skills,
            education = education,
            certification = certification
        )
        
    def get(self, request):

        user = request.user
        # profile = Profile.objects.create(user = user)
        # form = ApplicantForm(instance = profile, data = request.POST)
        try:
            person = user.profile
        except Profile.DoesNotExist:
            return redirect(reverse('accounts:details'))
        
        form = ApplicantForm()

        return render(request,'applicant.html',{'form':form}) 

class ApplicantDetails(views.View):

    def get(self, request, id):
        
        try:
            applicant = Applicant.objects.get(id = id)
        exccept Applicant.DoesNotExist:
            return redirect(reverse("jobs:all_job_app"))
            
        return render(request, 'applicant_details.html', {'applicant':applicant})
