from django import forms



class LocationForm(forms.Form):
    location = forms.CharField(label='')