from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def criar_view(request):
    if request.method == 'GET':
        form = UsuarioForm()
        return render(request, 'app/criar.html', {'form': form})
    elif request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:listar')


def listar_view(request):
    usuarios = Usuario.objects.all()
    return render(request, 'app/listar.html', {'usuarios': usuarios})


def atualizar_view(request, pk):
    usuarios = Usuario.objects.get(pk=pk)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuarios)
        return render(request, 'app/atualizar.html', {'form': form, 'usuarios': usuarios})
    elif request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
            return redirect('app:listar')

def deletar_view(request, pk):
    usuarios = Usuario.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'app/deletar.html', {'usuarios': usuarios})
    elif request.method == 'POST':
        usuarios.delete()
        return redirect('app:listar')

def detalhes_view(request, pk):
    usuarios = Usuario.objects.get(pk=pk)
    if usuarios:
        return render(request, 'app/detalhes.html', {'usuarios': usuarios})