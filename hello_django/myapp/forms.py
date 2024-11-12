from django import forms

class MyForm(forms.Form):
    firstname= forms.CharField()
    lastname = forms.CharField()
    