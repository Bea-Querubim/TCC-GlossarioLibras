from django.shortcuts import *
from django.db.models import Q
from .models import Palavra, Sinal
from .forms import *
from django.contrib.auth.decorators import login_required

def palavras_list(request):
    palavras = Palavra.objects.all()
    sinais = Sinal.objects.all()

    # Combina as listas de palavras e sinais usando zip
    palavras_sinais = zip(palavras, sinais)
    context = {'palavras_sinais': palavras_sinais}
    
    return render(request, 'glossario-3.html',context)


def palavras_new(request):          
    palavrasForm = PalavraForm(request.POST or None)
    # Valida e salva 
    if palavrasForm.is_valid():
        salvar = palavrasForm.save(commit=False)
        salvar.save()

        return redirect(sinal_new)
        
    else:
        return render(request, 'palavras.html', {'form1':palavrasForm});


def sinal_new(request):          
    sinalForm = SinalForm(request.POST or None, request.FILES) 
        
    # Valida e salva 
    if sinalForm.is_valid():
        salvar = sinalForm.save(commit=False)
        salvar.save()

        return redirect(palavras_list)
        
    else:
        return render(request, 'palavras.html', {'form2':sinalForm});



#home_search_palavras -> na pagina pincipal
def home_search_palavras(request):
    pesquisaHome = request.POST['pesquisaHome']
    try:
        lista = get_list_or_404(Palavra,nomePalavra=pesquisaHome)
        # procura exatamente o nome da plavra
        if(len(lista)==1):
            #mostrar a palavra relacionada aquela pesquisa
            palavraBanco = get_object_or_404(Palavra, nomePalavra=pesquisaHome)        
            sinalBanco = get_object_or_404(Sinal, nomePalavra=palavraBanco)
                
            contexto = {'palavra': palavraBanco, 'sinal': sinalBanco}
            return render(request, 'palavraBusca.html', contexto)
            
        else:
            print('dentro else - try')
            #mostrar lista de mais de uma palavra relacionada aquela pesquisa
            #lista = get_list_or_404(Palavra, nomePalavra=pesquisaHome)
            texto = 'Palavras relacionadas a sua pesquisa: '
            lista = Palavra.objects.filter(Q(nomePalavra__icontains=pesquisaHome))
            lista2 = Sinal.objects.filter(nomePalavra__in=lista)

            palavras_sinais = zip(lista, lista2)
            context = {'palavras_sinais': palavras_sinais, 'texto':texto}
            return render(request, 'glossario-3.html', context)
        
    except:
        #mostrar quando nao existe palavra cadastrada ou quando é um pedaço da palavra
        lista = Palavra.objects.filter(Q(nomePalavra__icontains=pesquisaHome))
        if(len(lista) == 0):
            # caso - nenhum resultado encontrado
            return render(request, 'glossario-3.html')
        else:
            # caso encontre uma ou mais palavras com esse contexto
            texto = 'Palavras relacionadas a sua pesquisa: '
            lista2 = Sinal.objects.filter(nomePalavra__in=lista)

            palavras_sinais = zip(lista, lista2)
            context = {'palavras_sinais': palavras_sinais,'texto':texto}
            return render(request, 'glossario-3.html', context)
        
        
def palavras_update(request):
    pass


#busca_nome_palavra_descricao -> na pagina de listagem de palavras
def buscar_palavra_descricao(request):
    idPesquisaLista = request.POST['idPesquisaLista']

    try:
        palavraLista = get_object_or_404(Palavra, idPalavra=idPesquisaLista)
        sinalLista = get_object_or_404(Sinal,idSinal=idPesquisaLista)
        
        context = {'palavra': palavraLista, 'sinal': sinalLista}
        return render(request, 'palavraBusca.html', context)
    
    except:
        #mostrar lista de palavras relacionada aquela pesquisa
        sinaisLista = Sinal.objects.filter(idSinal=idPesquisaLista)
        sinal = sinaisLista.first()
        palavrasLista = Palavra.objects.filter(idPalavra=idPesquisaLista)
        palavra = palavrasLista.first()
        
        context = {'palavra': palavra, 'sinal': sinal}
        return render(request, 'palavraBusca.html', context)



def palavras_buscar_disciplina():
    pass