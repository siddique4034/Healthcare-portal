from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

class PatientSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
            profile = Profile.objects.create(user=user,
                                             first_name=self.cleaned_data.get('first_name'),
                                             last_name=self.cleaned_data.get('last_name'),
                                             profile_picture=self.cleaned_data.get('profile_picture'),
                                             address_line1=self.cleaned_data.get('address_line1'),
                                             city=self.cleaned_data.get('city'),
                                             state=self.cleaned_data.get('state'),
                                             pincode=self.cleaned_data.get('pincode'))
        return user

class DoctorSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
            profile = Profile.objects.create(user=user,
                                             first_name=self.cleaned_data.get('first_name'),
                                             last_name=self.cleaned_data.get('last_name'),
                                             profile_picture=self.cleaned_data.get('profile_picture'),
                                             address_line1=self.cleaned_data.get('address_line1'),
                                             city=self.cleaned_data.get('city'),
                                             state=self.cleaned_data.get('state'),
                                             pincode=self.cleaned_data.get('pincode'))
        return user



