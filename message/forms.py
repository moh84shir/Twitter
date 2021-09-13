from django import forms


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
