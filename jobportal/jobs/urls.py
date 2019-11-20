from django.urls import path, include
from .views import JobView, JobDetails, PostedJobs, AllJobs, AllApplicationsForJob, ApplicationView, ApplicantAllApplications
from django.contrib.auth.decorators import login_required

app_name = 'jobs'

urlpatterns = [
    path('post/', login_required(JobView.as_view()), name='post_job'),
    path('<int:id>/details/', login_required(JobDetails.as_view()), name = 'job_details'),
    path('all/posted/', login_required(PostedJobs.as_view()), name='posted_jobs'),
    path('all/', login_required(AllJobs.as_view()), name='all_jobs'),
    path('<int:id>/applications/', login_required(AllApplicationsForJob.as_view()), name='all_job_app'),
    path('<int:id>/apply/', login_required(ApplicationView.as_view()), name='apply'),
    path('all/applied/', login_required(ApplicantAllApplications.as_view()), name='applied_jobs')
]
