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
        return redirect('volta_listagem')

    data['form'] = form

    return render (request, 'contas/form.html', data)