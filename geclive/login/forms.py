from django import forms
from login.models import UserProfile
from django.contrib.auth.models import User
from login.models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        #fields = ["username","password","first_name","last_name","email"]
	
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
	fields = ["dob","password","first_name","last_name","email"]

