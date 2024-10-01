from django import forms
from django.forms import ModelForm
from .models import *

class PalavraForm(ModelForm):
    class Meta:
       model =  Palavra
       fields = (
                'idPalavra',
                'nomePalavra',
                'descPalavra',
                'loginUsuario')
       widgets = {
           'idPalavra':forms.NumberInput(attrs={'class':'form-control'}),
            'nomePalavra':forms.TextInput(attrs={'class':'form-control'}),
            'descPalavra':forms.TextInput(attrs={'class':'form-control'}),
            'loginUsuario': setattr(Usuario, 'loginUsuario', Usuario.loginUsuario)
       }
       exclude=[
       ]
       
class SinalForm(ModelForm):
    class Meta:
       model =  Sinal
       fields = ('videoSinal',
                 'descSinalTexto',
                 'descSinalImagem',
                 'nomePalavra')
       widgets = {
            'descSinalTexto': forms.TextInput(attrs={'class': 'form-control'}),
            'videoSinal': forms.FileInput(),
            'descSinalImagem': forms.FileInput(),
            'nomePalavra': forms.Select(attrs={'class': 'form-control'}),
        }
       exclude=[
       ]
       
class UsuarioForm(ModelForm):
    class Meta:
        model =  Usuario
        fields = ('loginUsuario',
                 'senhaUsuario',
                 'nomeUsuario',
                 'emailUsuario')
        widgets = {
            'loginUsuario': forms.TextInput(attrs={'class':'form-control'}),
            'senhaUsuario': forms.PasswordInput(attrs={'class':'form-control'}),
            'nomeUsuario': forms.TextInput(attrs={'class':'form-control'}),
            'emailUsuario': forms.EmailInput(attrs={'class':'form-control'})
       }
        exclude=[
       ]
        