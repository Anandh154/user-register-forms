from app.models import *
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profilo
        fields=['address','picture']
