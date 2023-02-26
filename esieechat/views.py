from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .forms import ConversationUtilisateursForm, MessageForm, ConversationAddUtilisateurForm
from .models import Conversation, Message
from esieeverse.models import Utilisateur
from esieeverse.utils import check_utilisateur_auth

# Create your views here.
def create_conversation(request: HttpRequest) -> HttpResponse:
    """Affiche une vue permettant de créer une nouvelle conversation. 

    L'utilisateur pourra choisir avec qui il créer la conversation et comment elle se nommera

    Args:
        request (HttpRequest): La requête

    Returns:
        HttpResponse: Affiche la vue createconversation
        HttpResponseRedirect: Redirige l'utilisateur à la selection des conversation
    """
    if not check_utilisateur_auth(request):
        return redirect('/')

    form = ConversationUtilisateursForm()

    if request.method == 'POST':
        form = ConversationUtilisateursForm(request.POST)

        if form.is_valid():
            """ 
            Lorsque le formulaire est valide, on récupère les données afin de sauvegarder la conversation dans la BDD, 
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

    context = {
        'form': form,
        'return_arrow_btn_url': reverse('esieechat:select')
    }
    return render(request, 'conversation/createconversation.html', context)


def select_conversation(request: HttpRequest) -> HttpResponse:    
    """Vue permettant à l'utilisateur de sélectionner sa conversation

    Args:
        request (HttpRequest): La requête

    Returns:
        HttpResponse: Affiche la vue selectconversation
    """
    if not check_utilisateur_auth(request):
        return redirect('/')

    conversations = Conversation.objects.all()
    context = {
        'conversations': conversations,
        'return_arrow_btn_url': reverse('esieechat:create')
    }
    return render(request, 'conversation/selectconversation.html', context)


def view_conversation(request: HttpRequest, id_conversation: int) -> HttpResponse:
    """Vue permettant d'afficher un Chat avec l'ensemble des messages envoyés dans la conversation

    Args:
        request (HttpRequest): La requête
        id_conversation (int): id_conversation conversation

     Returns:
        HttpResponse: Affiche la vue pour afficher la conversation
    """
    if not check_utilisateur_auth(request):
        return redirect('/')

    if not Conversation.objects.filter(id=id_conversation).exists():
        return redirect('esieechat:select')

    form = MessageForm()

    messages = Message.objects.filter(conversation_id=id_conversation)
    utilisateur_conversation = Conversation.objects.filter(id=id_conversation)[0].utilisateurs

    context = {
        'form': form, 
        'messages': messages,
        'conversation_id': id_conversation,
        'utilisateurs_conversation': utilisateur_conversation.all(),
        'view': 'view_conversation',
        'return_arrow_btn_url': reverse('esieechat:select')
    }
    return render(request, 'conversation/viewconversation.html', context)

def add_people_in_conversation(request: HttpRequest, id_conversation: int) -> HttpResponse:
    """Permet d'ajouter des personnes à la conversation

    Args:
        request (HttpRequest): requête
        id_conversation (int): id_conversation conversation

    Returns:
        HttpResponse: Affiche la vue pour ajouter les personnes à la conversation
        HttpResponseRedirect: Redirige vers la conversation quand le formulaire est valide
    """
    if not check_utilisateur_auth(request):
        redirect('/')

    form = ConversationAddUtilisateurForm(id_conversation)

    if request.method == 'POST':
        form = ConversationAddUtilisateurForm(id_conversation, request.POST)

        if form.is_valid():
            
            users = form.cleaned_data['utilisateurs']

            conv = Conversation.objects.filter(id=id_conversation)[0]

            for user in users:
                conv.utilisateurs.add(user)
            
            return redirect('esieechat:view', id_conversation=id_conversation)

    context = {
        'form': form,
        'conversation_id': id_conversation,
        'return_arrow_btn_url': reverse('esieechat:view', kwargs={'id_conversation': id_conversation})
    }
    return render(request, 'conversation/addpeopleconversation.html', context)

def delete_people_in_conversation(request: HttpRequest, id_conversation: int, id_utilisateur: int) -> HttpResponse:
    """Permet de supprimer un utilisateur à la conversation

    Args:
        request (HttpRequest): requête
        id_conversation (int): id_conversation conversation
        id_utilisateur (int): id_conversation de l'utilisateur

    Returns:
        HttpResponse: Affiche la vue pour ajouter les personnes à la conversation
        HttpResponseRedirect: Redirige vers la conversation quand le formulaire est valide
    """
    if not check_utilisateur_auth(request):
        redirect('/')

    if request.method == 'POST' and request.POST.get('csrfmiddlewaretoken', None) != None:
        conversation = Conversation.objects.filter(id=id_conversation)[0]
        utilisateur_a_supprimer = Utilisateur.objects.filter(id=id_utilisateur)[0]
        conversation.utilisateurs.remove(utilisateur_a_supprimer)

    return redirect('esieechat:view', id_conversation=id_conversation)