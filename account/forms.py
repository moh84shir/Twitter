from django import forms


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

    email = forms.EmailField(
        max_length=120,
        label="Please Enter Your User Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
            }
        )
    )

    password = forms.CharField(
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