from django.shortcuts import render, redirect

from .forms import ConversationUtilisateursForm, MessageForm, ConversationAddUtilisateurForm
from .models import Conversation, Message
from esieeverse.models import Utilisateur
from django.contrib.auth.models import User

# Create your views here.
def create_conversation(request):
    """
    Affiche une vue permettant de créer une nouvelle conversation. 

    L'utilisateur pourra choisir avec qui il créer la conversation et comment elle se nommera
    """
    form = ConversationUtilisateursForm()

    if request.method == 'POST':
        form = ConversationUtilisateursForm(request.POST)

        if form.is_valid():
            """ Lorsque le formulaire est valide, on récupère les données afin de sauvegarder la conversation dans la BDD, 
                puis on redirige l'utilisateur vers la liste des conversations.
            """
            nom_conversation = form.cleaned_data['nom_conversation']
            users = form.cleaned_data['utilisateurs']

            conv = Conversation(nom=nom_conversation)
            conv.save()

            # On ajoute les utilisateurs à la conversations
            for user in users:
                conv.utilisateurs.add(user)
            
            conv.utilisateurs.add(request.user.utilisateur)

            return redirect('esieechat:select')

    context = {'form': form}
    return render(request, 'conversation/createconversation.html', context)


def select_conversation(request):
    """
    Vue permettant à l'utilisateur de sélectionner sa conversation
    """
    conversations = Conversation.objects.all()
    context = {'conversations': conversations}
    return render(request, 'conversation/selectconversation.html', context)


def view_conversation(request, id):
    """
    Vue permettant d'afficher un Chat avec l'ensemble des messages envoyés dans la conversation
    """
    form = MessageForm()
    
    if request.method == 'POST':
        form = MessageForm(request.POST)

        # Si le formulaire est valide alors on envoie le message dans la base de données 
        if form.is_valid():
            contenu_message = form.cleaned_data['contenu']
            message = Message(contenu=contenu_message, utilisateur=request.user.utilisateur, conversation_id=id)
            message.save()
            return redirect('esieechat:view', id=id)

    #messages = Message.objects.filter(conversation_id=id)
    context = {
        'form': form, 
        'utilisateur_connecte' : request.user.utilisateur,
        'conversation_id': id,
        'view': 'view_conversation'
    }
    return render(request, 'conversation/viewconversation.html', context)

def add_people_in_conversation(request, id):
    """
    Permet d'ajouter des personnes à la conversation
    """
    form = ConversationAddUtilisateurForm(id)

    if request.method == 'POST':
        form = ConversationAddUtilisateurForm(id, request.POST)

        if form.is_valid():
            
            users = form.cleaned_data['utilisateurs']

            conv = Conversation.objects.filter(id=id)[0]

            for user in users:
                conv.utilisateurs.add(user)
            
            return redirect('esieechat:view', id=id)

    context = {
        'form': form,
        'conversation_id': id,
    }
    return render(request, 'conversation/addpeopleconversation.html', context)