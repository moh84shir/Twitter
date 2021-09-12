from django import forms


class AddTweetForm(forms.Form):
    title = forms.CharField(
        max_length=120,
        label="Please Enter Your Tweet Titlte",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Tweet Titlte"
            }
        )
    )
    text = forms.CharField(
        max_length=120,
        label="Please Enter Your Tweet Text",
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tweet Text"
            }
        )
    )