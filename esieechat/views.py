from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseForbidden
from django.db.models import QuerySet
from .forms import CreateConversationUtilisateursForm, EditConversationUtilisateursForm, MessageForm, ConversationAddUtilisateurForm
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
        return redirect('auth:login')
    
    utilisateur_connecte: Utilisateur = request.user.utilisateur

    form = CreateConversationUtilisateursForm(utilisateur_connecte=utilisateur_connecte)

    if request.method == 'POST':
        form = CreateConversationUtilisateursForm(request.POST, utilisateur_connecte=utilisateur_connecte)

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
            
            conv.utilisateurs.add(utilisateur_connecte)

            return redirect('esieechat:select')

    context = {
        'form': form,
        'return_arrow_btn_url': reverse('esieechat:select')
    }
    return render(request, 'conversation/createconversation.html', context)

def create_or_join_conversation_with_user(request: HttpRequest, id_utilisateur: int) -> HttpResponseRedirect:
    """Créer ou rejoint une conversation avec uniquement l'id de l'utilisateur passé en paramètre et l'utilisateur connecté

    Args:
        request (HttpRequest): La requête HTTP
        id_utilisateur (int): L'id de l'utilisateur avec lequel on veut créer ou joindre une conversation

    Returns:
        HttpResponseRedirect: Une réponse HTTP de redirection vers la conversation créer ou joint
    """
    if not check_utilisateur_auth(request):
        return redirect('auth:login')
    
    utilisateur_connecte: Utilisateur = request.user.utilisateur
    utilisateur_to_send: Utilisateur = Utilisateur.objects.get(id=id_utilisateur)

    conversations: QuerySet = Conversation.objects.filter(utilisateurs=utilisateur_connecte).filter(utilisateurs=utilisateur_to_send)

    if conversations.exists():
        conversation = conversations[0]
    else:
        conversation = Conversation(nom=f"MP {utilisateur_connecte.user.first_name} - {utilisateur_to_send.user.first_name}")
        conversation.save()

        conversation.utilisateurs.add(utilisateur_connecte)
        conversation.utilisateurs.add(utilisateur_to_send)

    return redirect('esieechat:view', id_conversation=conversation.id)

def edit_conversation(request: HttpRequest, id_conversation: int) -> HttpResponse:
    """Permet de modifier la conversation passé en paramètre

    Args:
        request (HttpResponseRedirect): Une requête de redirection HTTP vers la vue de la conversation
        id_conversation (int): L'id de la conversation

    Returns:
        HttpResponse: La réponse HTTP
        HttpResponseForbidden: Si aucun token CSRF ou que la requête n'est pas post dans ce cas on retourne une erreur
    """    
    utilisateur_connecte: Utilisateur = request.user.utilisateur
    
    form = EditConversationUtilisateursForm(utilisateur_connecte=utilisateur_connecte, id_conversation=id_conversation)

    if request.method == 'POST':
        form = EditConversationUtilisateursForm(request.POST, utilisateur_connecte=utilisateur_connecte, id_conversation=id_conversation)
        if form.is_valid():
            """ 
            Lorsque le formulaire est valide, on récupère les données afin de modifier la conversation dans la BDD, 
            puis on redirige l'utilisateur vers la conversation.
            """

            nom_conversation = form.cleaned_data['nom_conversation']
            utilisateurs = form.cleaned_data['utilisateurs']

            conversation: Conversation = Conversation.objects.get(id=id_conversation)
            conversation.nom = nom_conversation
            conversation.utilisateurs.clear()

            for utilisateur in utilisateurs:
                conversation.utilisateurs.add(utilisateur)
            conversation.utilisateurs.add(utilisateur_connecte)

            conversation.save()

            return redirect('esieechat:view', id_conversation=id_conversation)
    
    context = {
        'form': form
    }

    return render(request, 'conversation/editconversation.html', context)

def select_conversation(request: HttpRequest) -> HttpResponse:    
    """Vue permettant à l'utilisateur de sélectionner sa conversation

    Args:
        request (HttpRequest): La requête

    Returns:
        HttpResponse: Affiche la vue selectconversation
    """
    if not check_utilisateur_auth(request):
        return redirect('auth:login')

    conversations = Conversation.objects.all()
    context = {
        'conversations': conversations,
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
        return redirect('auth:login')

    conversations = Conversation.objects.filter(id=id_conversation)

    if not conversations.exists():
        return redirect('esieechat:select')

    message_form = MessageForm()

    messages = Message.objects.filter(conversation_id=id_conversation)
    conversation: Conversation = conversations[0]

    context = {
        'message_form': message_form, 
        'messages': messages,
        'conversation': conversation,
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
        redirect('auth:login')

    utilisateur_connecte: Utilisateur = request.user.utilisateur

    form = ConversationAddUtilisateurForm(id_conversation=id_conversation, utilisateur_connecte=utilisateur_connecte)

    if request.method == 'POST':
        form = ConversationAddUtilisateurForm(request.POST, id_conversation=id_conversation, utilisateur_connecte=utilisateur_connecte)

        if form.is_valid():
            
            users = form.cleaned_data['utilisateurs']

            conv = Conversation.objects.get(id=id_conversation)

            for user in users:
                conv.utilisateurs.add(user)
            
            return redirect('esieechat:view', id_conversation=id_conversation)

    context = {
        'form': form,
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
        redirect('auth:login')

    if request.method == 'POST' and request.POST.get('csrfmiddlewaretoken', None) != None:
        conversation: Conversation = Conversation.objects.get(id=id_conversation)
        utilisateur_a_supprimer: Utilisateur = Utilisateur.objects.get(id=id_utilisateur)
        conversation.utilisateurs.remove(utilisateur_a_supprimer)

    return redirect('esieechat:view', id_conversation=id_conversation)