from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# user login form
class LogInForm(forms.Form):
   username = forms.CharField(max_length=55)
   password = forms.CharField(widget=forms.PasswordInput)


# user registration form
class UserRegistrationForm(UserCreationForm):
       class Meta:
             model = User
             fields = ['username','first_name','last_name','email','password1','password2']
             help_texts = {
            'username': None,
            'email': None,
            # 'password1': None,
            # 'password2': None,
        }

   