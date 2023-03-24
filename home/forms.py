from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
# Le reste sera a ajouter pour la suite