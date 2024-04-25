from django.shortcuts import render
from .models import cadastro

# Create your views here.

def home(request):
    return render(request, 'aluno/home.html')

def gravar(request):
    novo = cadastro()
    novo.nome = request.POST.get('nome')
    novo.sobrenome = request.POST.get('sobrenome')
    novo.idade = request.POST.get('idade')
    novo.save()

    gravar = {
        'gravar': cadastro.objects.all()
    }

    return render(request, 'aluno/resultado.html', gravar)