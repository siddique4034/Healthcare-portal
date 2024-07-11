from django.shortcuts import render, redirect
from .forms import PatientSignupForm, DoctorSignupForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_patient:
            return reverse_lazy('patient_dashboard')
        elif user.is_doctor:
            return reverse_lazy('doctor_dashboard')
        else:
            return reverse_lazy('login')

def home_page(request):
    return render(request, 'accounts/home.html')

def signup(request):
    return render(request, 'accounts/signup.html')

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientSignupForm()
    return render(request, 'accounts/signup_form.html', {'form': form, 'user_type': 'Patient'})

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('doctor_dashboard')
    else:
        form = DoctorSignupForm()
    return render(request, 'accounts/signup_form.html', {'form': form, 'user_type': 'Doctor'})

@login_required(login_url='login/')
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html')

@login_required(login_url='login/')
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html')

