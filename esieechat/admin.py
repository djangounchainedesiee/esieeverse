from django.contrib import admin
from .models import Message, Conversation, ConvUtilisateur

# Register your models here.
admin.site.register(Conversation)
admin.site.register(ConvUtilisateur)
admin.site.register(Message)