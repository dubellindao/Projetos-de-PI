from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    duracao = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    image_curso = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome

class Hobbies(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)
    image_hobbie = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome