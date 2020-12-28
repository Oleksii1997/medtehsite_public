"""medtehsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from.import views

urlpatterns = [
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),
	path('registation/', views.registration_new_user, name="registration_new_user"),
    path('recovery_password/', views.recovery_password, name="recovery_password"),
    path('change_password_form/', views.change_password_form, name="change_password_form"),
    path('change_password/', views.change_password, name="change_password"),
]
