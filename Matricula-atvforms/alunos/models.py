from django.db import models

# Create your models here.

class Aluno (models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    cidade = models.CharField(max_length=100, choices=[
        ('lg', 'Luís Gomes'),
        ('pdf', 'Pau dos Ferros'),
        ('sm', 'São Miguel')
    ])
    curso = models.CharField(max_length=100, choices=[
        ('info', 'Informática'),
        ('api','Apicultura'),
        ('ali', 'Alimentos')
    ])

    def __str__(self):
        return self.nome