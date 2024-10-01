from django.shortcuts import render, redirect
from .models import palavra, sinal
from .forms import PalavraForm, SinalForm
from django.views import generic

# 'palavras' é a variavel que será passado para a pagina html, e usada no for para a leitura dos dados.


class palavras_list(generic.ListView):
    model = palavra
    palavras = palavra.objects.all()
    sinais = sinal.objects.all()


def palavras_new(request):          
    palavrasForm = PalavraForm(request.POST or None)
    sinalForm = SinalForm(request.POST or None, request.FILES)  
    

    # Valida e salva 
    if palavrasForm.is_valid():
        salvar = palavrasForm.save(commit=False)
        salvar.save()
       
        if sinalForm.is_valid():
            salvar2 = sinalForm.save(commit=False)
            salvar2.save()
        
            return redirect("palavras_list")
        
    else:
        return render(request, 'palavras.html', {'form1':palavrasForm,'form2':sinalForm});


def palavras_update(request):
    pass


def list_palavras_byNome(request):
    pass    




