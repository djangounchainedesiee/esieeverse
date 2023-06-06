from django import forms

class SettingForm(forms.Form):
    first_name = forms.CharField(
        label="Prénom",
        max_length=50,
        required = False,   
        widget=forms.TextInput()
    )

    last_name = forms.CharField(
        label="Nom",
        max_length=50,
        required = False,   
        widget=forms.TextInput()
    )

    login = forms.CharField(
        label="Login",
        max_length=50,
        required = False,   
        widget=forms.TextInput()
    )

    email = forms.CharField(
        label="Adresse mail",
        max_length=50,
        required = False,   
        widget=forms.TextInput()
    )

    photo_de_profile = forms.ImageField(
        required=False,    
        label="Photo de Profile",
        widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
    )

    password = forms.CharField(
        label="Mot de passe",
        max_length=50,
        required = False,   
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
