from django import forms
from .models import Profile, Applicant

class ProfileForm(forms.ModelForm):

    is_recruiter = forms.BooleanField(
        required=False,
        label = "Are you a recruiter?"
    )

    class Meta:
        model = Profile
        fields = ['name',
                    'occupation',
                    'company_name',
                    'is_recruiter',
                    'gender'
                ]

class ApplicantForm(forms.ModelForm):

    is_student = forms.BooleanField(
        required=False,
        label = "Are you a student?"
    )
    # decription = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder': "Add an intrduction to yourself."})
    # )
    # skills = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder': "Enter skills separated by commas."})
    # )
    # education = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder': "Enter education details, i.e., institute name, course, score."})
    # )
    # certification = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder': "Enter certification details, i.e, course name, short description."})
    # )

    class Meta:
        model = Applicant
        fields = [
                    'is_student',
                    'experience',
                    'description',
                    'skills',
                    'education',
                    'certification'
                ]