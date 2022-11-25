from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ConversationUtilisateursForm
from .models import ConvUtilisateur, Conversation
from django.contrib.auth.models import User

# Create your views here.
def create_conversation(request):
    form = ConversationUtilisateursForm()
    print(request.POST)
    if request.method == 'POST':
        form = ConversationUtilisateursForm(request.POST)

        if form.is_valid():
            print('FORM IS VALID ! ')
            nomConversation = form.cleaned_data['nomConversation']
            usersId = form.cleaned_data['utilisateurs']

            conv = Conversation(nom=nomConversation)
            conv.save()
            for userId in usersId:
                convUser = ConvUtilisateur(
                    idConversation=conv.id, idUtilisateur=userId)
                convUser.save()

            return HttpResponseRedirect('conversation/selectconversation.html')
    context = {'form': form}
    return render(request, 'conversation/createconversation.html', context)


def select_conversation(request):
    conversationsUtilisateurs = ConvUtilisateur.objects.filter(
        idUtilisateur=request.user.id).values('idConversation')
    conversations = Conversation.objects.filter(
        pk__in=[conversationsUtilisateurs])

    context = {'conversations': conversations}
    return render(request, 'conversation/selectconversation.html', context)

def view_conversation(request, id):
    context = {'messages': []}
    return render(request, 'conversation/viewconversation.html', context)
