from django.shortcuts import render, redirect

from .forms import ConversationUtilisateursForm, MessageForm
from .models import Conversation, Message
from esieeverse.models import Utilisateur
from django.contrib.auth.models import User

# Create your views here.
def create_conversation(request):
    form = ConversationUtilisateursForm()
    #print('form : ' , form)
    if request.method == 'POST':
        form = ConversationUtilisateursForm(request.POST)

        if form.is_valid():
            nom_conversation = form.cleaned_data['nom_conversation']
            users = form.cleaned_data['utilisateurs']

            conv = Conversation(nom=nom_conversation)
            
            
            print('Users : ', users)
            conv.save()

            for user in users:
                print('User : ', user)
                conv.utilisateurs.add(user)
            
            print('Save conversation : ', conv)

            return redirect('esieechat:select')

    context = {'form': form}
    return render(request, 'conversation/createconversation.html', context)


def select_conversation(request):
    conversations = Conversation.objects.all()
    context = {'conversations': conversations}
    return render(request, 'conversation/selectconversation.html', context)


def view_conversation(request, id):
    form = MessageForm()
    
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            contenu_message = form.cleaned_data['contenu']
            print("User : ", request.user.utilisateur)
            message = Message(contenu=contenu_message, utilisateur=request.user.utilisateur, conversation_id=id)
            print("Enregistrement du message : ", message)
            message.save()

    messages = Message.objects.filter(conversation_id=id)
    context = {
        'form': form, 
        'messages': messages,
        'utilisateur_connecte' : request.user,
        'view_id': id
    }
    return render(request, 'conversation/viewconversation.html', context)
