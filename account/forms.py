from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class SigninForm(forms.Form):
    user_name = forms.CharField(
        max_length=120,
        label="Please Enter Your User Name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "User Name",
            }
        )
    )

    password = forms.CharField(
        max_length=120,
        label="Please Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "User Name",
            }
        )
    )


class SignupForm(forms.Form):
    user_name = forms.CharField(
        max_length=120,
        label="Please Enter Your User Name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "User Name",
            }
        )
    )

    user_first_name = forms.CharField(
        max_length=120,
        label="Please Enter Your First Name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name"
            }
        )
    )

    user_last_name = forms.CharField(
        max_length=120,
        label="Please Enter Your Last Name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name"
            }
        )
    )


    user_email = forms.EmailField(
        max_length=120,
        label="Please Enter Your User Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
            }
        )
    )

    user_password = forms.CharField(
        max_length=120,
        label="Please Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
            }
        )
    )

    re_password = forms.CharField(
        max_length=120,
        label="Please Enter Your Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
            }
        )
    )
