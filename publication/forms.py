from django import forms


class CreatePublicationForm(forms.Form):
    titre = forms.CharField(
        max_length=100, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    contenu = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    attachment = forms.FileField(
        required=False, 
        label="Pièce jointe", 
        widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
    )

class CreateChoiceForm(forms.Form):
    nom = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        error_messages={'required': 'Le champ titre est obligatoire.'}
    )
class CreateEvenementForm(forms.Form):
    titre = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        error_messages={'required': 'Le champ titre est obligatoire.'}
    )
    date_debut = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True,
        error_messages={'required': 'Le champ date de début est obligatoire.'}
    )
    date_fin = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True,
        error_messages={'required': 'Le champ date de fin est obligatoire.'}
    )
    contenu = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=True,
        error_messages={'required': 'Le champ contenu est obligatoire.'}
    )
    attachment = forms.FileField(
        required=False,
        label="Pièce jointe",
        widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
    )
    choixs_formset = forms.formset_factory(CreateChoiceForm, extra=0)
