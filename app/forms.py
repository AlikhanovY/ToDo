from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import Profile

from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=['title']

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=30)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Password confirmation")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        profile = Profile(user= user, first_name=self.cleaned_data['first_name'],
                          last_name=self.cleaned_data['last_name']
                          )
        if commit:
            profile.save()

        return profile

    def clean_username(self):
        username = self.cleaned_data['username']
        new = User.objects.filter(username= username)
        if new.count():
            raise forms.ValidationError("User already exists!")

        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        print("Password1:", password1)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords doesnt match!")

        return password2

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = ['username', 'password']




