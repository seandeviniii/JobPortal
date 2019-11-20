from django import forms
from .models import Job, Application

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['title',
                    'description',
                    'pay',
                    'last_date'
                ]

