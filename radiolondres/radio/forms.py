from django import forms


class diffuser_message (forms.Form):
    resistant = forms.CharField(max_length=50)
    message = forms.CharField(max_length=255)