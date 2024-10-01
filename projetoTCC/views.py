from django.shortcuts import *
from glossarioLibras.forms import *
from glossarioLibras.views import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import *

def sign(request):
    sign = UsuarioForm(request.POST or None)
    if sign.is_valid():
        sign.save()
        return redirect(home)
        
    else:
        return render(request, 'registration/sign.html', {'sign':sign});


def login(request):
    try:
        if request.method == 'POST':
                
            request.session['usuario_autenticado'] = False  # muda o valor para quando ele estuver autenticado
            user = request.POST.get('loginUsuario')
            passw = request.POST.get('senhaUsuario')

            usuario = Usuario.objects.filter(loginUsuario=user).first()
            senha_valida = Usuario.objects.filter(senhaUsuario=passw).exists()
            
            if usuario is None:
                return render(request, 'registration/login.html', {'error_message': 'Usuário não encontrado'})
        
            elif not senha_valida:
                return render(request, 'registration/login.html', {'error_message': 'Senha invalida'})
                
            else:
                request.session['usuario_autenticado'] = True  # muda o valor para quando ele estuver autenticado
                request.session['nome_usuario'] = user  # Armazena o nome de usuário na sessão
                return redirect(home)

    except Exception as e:
        return render(request, 'registration/login.html', {'error_message': 'Ocorreu um erro ao processar o login, tente novamente'})
    
    return render(request, 'registration/login.html', {})


def logout_view(request):
    
    logout(request)
    request.session['usuario_autenticado'] = False  # muda o valor para quando ele fizer logout
    return redirect(home)
    

def home(request):
    return render(request, "index2.html");