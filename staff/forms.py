from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'id_email', 'autofocus': 'true', 'placeholder': 'Email Address', 'required': 'true'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'id_username', 'placeholder': 'Username', 'required': 'true'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'id_password1', 'placeholder': 'Password', 'required': 'true'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'id_password2', 'placeholder': 'Confirm Password', 'required': 'true'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'id_username', 'autofocus': 'true', 'placeholder': 'Username', 'required': 'true'}))
   
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'id_password', 'placeholder': 'Password', 'required': 'true'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    "This user Does Not exists in the system")
            if not user.check_password(password):
                raise forms.ValidationError("Password Incorrect")
            if not user.is_active:
                raise forms.ValidationError(
                    "User Is No longer Active. Contact Admin")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class StaffProfileForm(forms.ModelForm):
    """Form definition for StaffProfile."""
    lecturer_sirname = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'id': 'id_lecturer_sirname', 'autofocus': 'true', 'required': 'true'}))
    other_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'id': 'id_other_name', 'required': 'true'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'id': 'id_email', 'required': 'true'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'id': 'id_address', 'required': 'true'}))
    tel = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'id': 'id_tel', 'required': 'true'}))
    user_id_or_pe_nember = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'id': 'id_user_id_or_pe_nember', 'required': 'true'}))
   

    class Meta:
        """Meta definition for StaffProfileform."""

        model = StaffProfile
        fields = ['lecturer_sirname', 'other_name', 'email', 'address','tel', 'user_id_or_pe_nember']

class UnitForm(forms.ModelForm):
    """Form definition for Unit."""
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'id': 'id_name', 'autofocus': 'true', 'required': 'true'}))
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'id': 'id_code', 'autofocus': 'true', 'required': 'true'}))

    class Meta:
        """Meta definition for Unitform."""
        model = Unit
        fields = ['name', 'code']

class AccademicSessionForm(forms.ModelForm):
    """Form definition for AccademicSession."""
    semester = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'id': 'id_semester', 'autofocus': 'true', 'required': 'true'}))
    accademic_year = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'id': 'id_accademic_year', 'autofocus': 'true', 'required': 'true'}))
    session = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'id': 'id_session', 'autofocus': 'true', 'required': 'true'}))

    class Meta:
        """Meta definition for AccademicSessionform."""
        model = AccademicSession
        fields = ['semester', 'accademic_year', 'session']


class ReportForm(forms.ModelForm):
    """Form definition for Report."""

    class Meta:
        """Meta definition for Reportform."""

        model = Report
        fields = ['unit', 'staffprofile', 'accademicsession']

