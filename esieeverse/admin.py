from django.contrib import admin
from .models import Utilisateur, Classe, Filiere, Promotion

admin.site.register(Utilisateur)
admin.site.register(Classe)
admin.site.register(Filiere)
admin.site.register(Promotion)