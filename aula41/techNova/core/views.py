from django.shortcuts import redirect, render
from .models import Servico, Curso
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def servicos(request):
    servicos = Servico.objects.all()  # Busca todos os registros da tabela Servico
    return render(request, 'servicos.html', {'servicos': servicos})

def registrarUsuario(request):
    if request.method == 'POST':
        nome_usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = User.objects.create_user(username=nome_usuario, password=senha)
        user.save()
    return render(request, 'registrar-usuario.html') 

def custom_logout(request):
    logout(request)
    return render('home.html')

def login(request):
    return render(request, 'login.html')