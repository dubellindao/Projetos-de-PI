from django.shortcuts import render, redirect
from .forms import Aluno
from .forms import AlunoForm

# Create your views here.

def forms_alunos(request):

    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no banco de dados
            return redirect('forms')  # Redireciona após o sucesso
    else:
        form = AlunoForm()

    context = {
        'form': form
    }

    return render(request, 'alunos/forms.html', context)


def listar_alunos(request):

    alunos = Aluno.objects.all()
    context = {
        'list_alunos': alunos
    }

    return render (request, 'alunos/listagem_alunos.html', context)