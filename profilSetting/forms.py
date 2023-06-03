from django import forms

class SettingForm(forms.Form):
    password = forms.CharField(
        label="Mot de passe",
        max_length=50,
        required = False,   
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    photo_de_profile = forms.ImageField(
        required=False,    
        label="Photo de Profile",
        widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
    )
