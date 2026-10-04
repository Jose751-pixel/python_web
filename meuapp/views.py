from django.shortcuts import render
from .models import Contato

def index(request):
    return render(request, 'meuapp/page.html')

def contatos(request):
    contatos = Contato.objects.order_by('date_added') 
    context = {'contatos': contatos} 
    return render(request, 'meuapp/contatos.html', context) 