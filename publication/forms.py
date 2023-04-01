from django import forms

class PostForm(forms.Form):
    titre = forms.CharField(max_length=100)
    contenu = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False, label="Pièce jointe")

# Le reste sera a ajouter pour la suite