from django.urls import path
from .views import signup, RegisterView, ApplicantView, GetHome, GetDashboard, ApplicantDetails
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = 'accounts'

urlpatterns = [
    path('', GetHome.as_view(), name='home'),
    path('dashboard/', login_required(GetDashboard.as_view()), name='dashboard'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('details/', login_required(RegisterView.as_view()), name='details'),
    path('applicant/', login_required(ApplicantView.as_view()), name='applicant'),
    path('applicant/<int:id>/details/', login_required(ApplicantView.as_view()), name='applicant_details')
]