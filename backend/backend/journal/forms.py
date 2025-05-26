from django import forms

class EntryForm(forms.Form):
    entry = forms.CharField(label = "entry", max_length=500)