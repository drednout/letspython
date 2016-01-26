from django import forms


class PlayerChangeForm(forms.Form):
    name = forms.CharField(label='Name', max_length=45)
    email = forms.EmailField(label='Email')
