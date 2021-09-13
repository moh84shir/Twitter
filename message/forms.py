from django import forms
from django.contrib.auth.models import User


class SendMessageForm(forms.Form):
    title = forms.CharField(
        max_length=120,
        label="Enter Message Title",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Message Title"
            }
        )
    )

    text = forms.CharField(
        max_length=120,
        label="Enter Message Text",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Message Text"
            }
        )
    )

    subject = forms.CharField(
        max_length=120,
        label="Enter Message Subject",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Message Subject"
            }
        )
    )

    to_user = forms.CharField(
        max_length=120,
        label="Enter Message User",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Message User"
            }
        )
    )


    def clean_to_user(self):
        to_user = self.cleaned_data.get("to_user")
        is_user_exists = User.objects.filter(username=to_user).exists()

        if not is_user_exists:
            raise forms.ValidationError('user is not exists')

        return to_user