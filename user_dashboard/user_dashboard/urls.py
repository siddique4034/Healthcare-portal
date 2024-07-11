"""
URL configuration for user_dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from accounts.views import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', accounts_views.home_page, name='signup'),
    path('signup/', accounts_views.signup, name='signup'),
    path('signup/patient/', accounts_views.patient_signup, name='patient_signup'),
    path('signup/doctor/', accounts_views.doctor_signup, name='doctor_signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('patient_dashboard/', accounts_views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', accounts_views.doctor_dashboard, name='doctor_dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



