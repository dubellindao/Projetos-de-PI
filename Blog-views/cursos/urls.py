from django.contrib import admin
from django.urls import path
from cursos.views import index, alimentos, quimica, ads

urlpatterns = [
    path('', index,name='index') ,
    path('alimentos/', alimentos, name='alimentos'),
    path('quimica/', quimica, name='quimica'),
    path('ads/', ads, name='ads'),
]