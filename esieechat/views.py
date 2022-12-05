from django.shortcuts import render, redirect

from .forms import ConversationUtilisateursForm, MessageForm
from .models import Conversation, Message
from django.contrib.auth.models import User

# Create your views here.


def create_conversation(request):
    form = ConversationUtilisateursForm()
    print('form : ' , form)
    if request.method == 'POST':
        form = ConversationUtilisateursForm(request.POST)

        if form.is_valid():
            nom_conversation = form.cleaned_data['nom_conversation']
            users = form.cleaned_data['utilisateurs']

            conv = Conversation(nom=nom_conversation)
            
            print('Save conversation : ', conv)
            
            for user in users:
                conv.utilisateurs.add(user)
            
            conv.utilisateurs.add(request.user)
            conv.save()

            return redirect('esieechat:select')

    context = {'form': form}
    return render(request, 'conversation/createconversation.html', context)


def select_conversation(request):
    conversations = Conversation.objects.all().values('conversation_id')
    context = {'conversations': conversations}
    return render(request, 'conversation/selectconversation.html', context)


def view_conversation(request, id):
    form = MessageForm()
    
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            contenu_message = form.cleaned_data['contenu']
            message = Message(contenu=contenu_message, utilisateur=request.user, conversation_id=id)
            message.save()

    messages = Message.objects.filter(conversation_id=id)
    context = {
        'form': form, 
        'messages': messages
    }
    return render(request, 'conversation/viewconversation.html', context)
