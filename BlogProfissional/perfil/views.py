from django.shortcuts import render
from perfil.models import Curso, Hobbies

# Create your views here.

def index (request):
    cursos = Curso.objects.all()
    hobbies = Hobbies.objects.all()

    context = {
        'list_cursos': cursos,
        'list_hobbies': hobbies,
    }

    return render(request, 'perfil/index.html', context)

def sobre (request):
    return render(request, 'perfil/sobre.html')