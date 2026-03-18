from django.shortcuts import render,redirect
from  .models import Pessoa
from .forms import PessoaForm

'''def home(request):
    return render(request,'meuapp/home.html')'''
# Create your views here.

def listar_pessoas(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'meuapp/list.html', {'pessoas': pessoa})


def criar_pessoas(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else: 
        form = PessoaForm()
    return render(request, 'meuapp/form.html', {'form': form})
