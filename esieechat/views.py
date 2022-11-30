from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ConversationUtilisateursForm, MessageForm
from .models import ConvUtilisateur, Conversation, Message
from django.contrib.auth.models import User

# Create your views here.


def create_conversation(request):
    form = ConversationUtilisateursForm()
    print('form : ' , form)
    if request.method == 'POST':
        form = ConversationUtilisateursForm(request.POST)

        if form.is_valid():
            print('Create conversation form is valid ! ')
            nom_conversation = form.cleaned_data['nom_conversation']
            users = form.cleaned_data['utilisateurs']

            conv = Conversation(nom=nom_conversation)
            
            print('Save conversation : ', conv)
            conv.save()
            for user in users:
                conv_user = ConvUtilisateur(conversation_id=conv.id, utilisateur_id=user.id)
                conv_user.save()

            return HttpResponseRedirect('conversation/selectconversation.html')
    context = {'form': form}
    return render(request, 'conversation/createconversation.html', context)


def select_conversation(request):
    conversations_utilisateurs = ConvUtilisateur.objects.filter(
        utilisateur_id=request.user.id).values('conversation_id')
    conversations = Conversation.objects.filter(
        pk__in=[conversations_utilisateurs])

    context = {'conversations': conversations}
    return render(request, 'conversation/selectconversation.html', context)


def view_conversation(request, id):
    form = MessageForm()
    
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            contenu_message = form.cleaned_data['contenu']
            message = Message(contenu=contenu_message)
            message.save()

    messages = Message.objects.filter(conversation_id=id)
    context = {
        'form': form, 
        'messages': messages
    }
    return render(request, 'conversation/viewconversation.html', context)
