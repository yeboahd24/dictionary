from django import forms


class WordForm(forms.Form):
    input = forms.CharField(label="Enter a sentence or paragraph:")
