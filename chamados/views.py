from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ChamadoForm
from .models import Chamado

def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('painel_usuario')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def painel_usuario_view(request):
    chamados = Chamado.objects.filter(solicitante=request.user).order_by('-data_abertura')
    return render(request, 'painel_usuario.html', {'chamados': chamados})
     
#Criar view: Novo chamado
@login_required
def novo_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            chamado = form.save(commit=False)
            chamado.solicitante = request.user
            chamado.save()
            return redirect('painel_usuario')
    else:
        form = ChamadoForm()
    return render(request, 'chamados/novo_chamado.html', {'form': form})