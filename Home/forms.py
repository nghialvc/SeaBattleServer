from django import forms
import re
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=15)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=15)
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password',widget=forms.PasswordInput)

    def clear_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+&', username):
            raise forms.ValidationError("Username is invalid")
        try:
            User.objects.get(username=username)
        except:
            return username
        raise forms.ValidationError("Username was existed")

    def clear_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise form.ValidationError("Password is invalid")
        
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],password=self.cleaned_data['password1'])
