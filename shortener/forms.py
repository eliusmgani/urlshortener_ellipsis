from django import forms
from . models import UrlShortener, CustomUser
from django.forms import ModelForm
from django.forms import URLInput, NumberInput, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class UrlForm(ModelForm):
    class Meta:
        model = UrlShortener
        fields = ["original_url", "lifespan"]
        widgets = {
            "original_url": URLInput(attrs={
                "type": "url",
                "placeholder": "long url",
                "class": "form-control"
            }),
            "lifespan": NumberInput(attrs={
                "type": "number",
                "placeholder": "life span",
                "class": "form-control"
            }),
        }
        labels = {
            "original_url": _("Long URL"),
        }

        help_texts = {
            "original_url": _("write an URL starts with http"),
            "lifespan": _("enter life span in seconds"),
        }


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "mobile_no", "profile_pic"]
        exclude = ["password1", "password2"]
        widgets = {
            "first_name": TextInput(attrs={
                "placeholder": "first name",
                "class": "form-control"
            }),
            "last_name": TextInput(attrs={
                "placeholder": "last name",
                "class": "form-control"
            }),
            "username": TextInput(attrs={
                "placeholder": "username",
                "class": "form-control"
            }),
            "mobile_no": NumberInput(attrs={
                "type": "number",
                "placeholder": "mobile number",
                "class": "form-control"
            }),
        }
        help_texts = {
            "mobile_no": _("put number starts with 0"),
        }
        labels = {
            "mobile_no": _("Mobile No:")
        }
