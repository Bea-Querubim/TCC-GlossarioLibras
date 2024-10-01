from django.urls import path
from .views import *
from glossarioLibras.views import *

urlpatterns = [
    path('', palavras_list, name='palavras_list'),
    path('cadastrar/palavra', palavras_new, name="palavras_new"),
    path('cadastrar/sinal', sinal_new, name="sinal_new"),
    path('atualizar/', palavras_update, name="palavras_update"),
    path('buscar/lista', home_search_palavras, name="home_search_palavras"),
    path('buscar/palavra', buscar_palavra_descricao, name="buscar_palavra_descricao"),

    path('buscar/disciplina/<int:pk>', palavras_buscar_disciplina, name="palavras_disciplina"),
]