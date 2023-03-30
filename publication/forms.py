from django import forms

from .models import Publication

class PostForm(forms.Form):
    titre = forms.CharField(max_length=100)
    contenu = forms.CharField(widget=forms.Textarea)

# Le reste sera a ajouter pour la suite