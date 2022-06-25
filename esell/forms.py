from esell.models import Customer
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
from django.utils.translation import gettext, gettext_lazy as _

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'current-password', 'class':'form-control'}))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus':True, 'class':'form-control'}))
    
    new_password1 = forms.CharField(label=_('New Password'), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), 
    help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(label=_('Confirm  New Password'), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))



class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, 
    widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'}))


class ConfirmPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','delivary_mail','village', 'division', 'district', 'postal' ]
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}), 'delivary_mail':forms.TextInput(attrs={'class':'form-control'}), 'village':forms.TextInput(attrs={'class':'form-control'}), 'district':forms.TextInput(attrs={'class':'form-control'}), 'postal':forms.NumberInput(attrs={'class':'form-control'}),'division':forms.Select(attrs={'class':'form-control'}),}
