from django.urls import path
from .views import forms_alunos, listar_alunos

urlpatterns = [
    path('', forms_alunos, name='forms'),
    path('listagem_alunos/', listar_alunos, name='listar_alunos'),
]