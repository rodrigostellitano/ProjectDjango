from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from .form import TransacaoForm


def home(request):
        
    return render(request, "contas/home.html")

def listagem(request):
    data = {}
    
    data['transacoes'] = Transacao.objects.all()

    return render(request,"contas/listagem.html", data)



def nova_transacao(request):
    data = {}
    
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form

    return render (request, 'contas/form.html', data)


def update(request, pk):
    data = {}

    #Pega o que retorna no banco e adiciona na variavel
    transacao = Transacao.objects.get(pk=pk)

    #Pega a transação em cima e preenche o formulário
    form = TransacaoForm(request.POST or None, instance=transacao)


    #Qualquer mudança e salva nesse formulário que pegou e volta para a lista
    if form.is_valid():
            form.save()
            return redirect('url_listagem')
    
    data['form'] = form
    data['transacao'] = transacao

    return render (request, 'contas/form.html', data)




def delete(request,pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()


    return redirect('url_listagem')