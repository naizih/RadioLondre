from django import forms


class contact_us_Form (forms.Form):
    resistant = forms.CharField(max_length=50)
    message = forms.CharField(max_length=255)