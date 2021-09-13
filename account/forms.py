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

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')

        is_user_exists_by_username = User.objects.filter(
            username=user_name).exists()
        if is_user_exists_by_username:
            raise forms.ValidationError('this user is exists')

        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('user_password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('password != re password')

        return password

    def clean_user_email(self):
        user_email = self.cleaned_data.get('user_email')

        is_user_exists_by_email = User.objects.filter(
            email=user_email).exists()

        if is_user_exists_by_email:
            raise forms.ValidationError('this user is exists')

        return user_email