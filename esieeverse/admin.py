from django.contrib import admin
from .models import Utilisateur, Filiere, Promotion

admin.site.register(Utilisateur)
admin.site.register(Filiere)
admin.site.register(Promotion)