from django import forms


class SettingForm(forms.Form):
    password = forms.CharField(
        label="Mot de passe",
        max_length=50,
        required = False,   
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    PhotoProfile = forms.FileField(
        required = False,    
        label="Photo Profile",
        widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
    )
