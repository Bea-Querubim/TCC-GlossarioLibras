from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.AutoField(verbose_name="idUsuario", unique=True,primary_key=True, auto_created=True,null=False, blank=False)
    loginUsuario = models.CharField(max_length=200,verbose_name="Login", unique=True)
    senhaUsuario = models.CharField(max_length=200,verbose_name="Senha")
    nomeUsuario = models.CharField(max_length=200,verbose_name="Nome Completo")
    emailUsuario = models.EmailField(max_length=200,verbose_name="Email", unique=True)
    
    
    def __str__(self):
            return self.loginUsuario
        
    class Meta:
        managed:False
        db_table = 'Usuario'


class Palavra(models.Model):
    idPalavra = models.AutoField(verbose_name="idPalavra", unique=True,primary_key=True, auto_created=True,null=False, blank=False)
    nomePalavra = models.CharField(max_length=200,verbose_name="Palavra", null=False, blank=False)
    descPalavra = models.CharField(max_length=500,verbose_name="Descricao", null=False, blank=False)
    
    loginUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name="Usuario responsavel",blank=True)
    
    def __str__(self):
            return self.nomePalavra
        
    class Meta:
        managed:False
        db_table = 'Palavra'

  
class Sinal(models.Model):
    nomePalavra = models.ForeignKey(Palavra, on_delete=models.CASCADE, verbose_name="Palavra referente", related_name='palavra')
    idSinal = models.AutoField(verbose_name="Id Sinal", unique=True, primary_key=True, auto_created=True)
    videoSinal = models.FileField(upload_to='uploads/videoSinal', verbose_name="Video", null=False, blank=False)
    descSinalTexto = models.CharField(max_length=500, verbose_name="Descricao Sinal em Texto", null=False, blank=False)
    descSinalImagem = models.ImageField(upload_to='uploads/imageSinal', verbose_name="Imagem", null=False, blank=False)

    def __str__(self):
            return self.nomePalavra.nomePalavra

        
    class Meta:
        managed:False
        db_table = 'Sinal'

       
class Curso(models.Model):
    siglaCurso = models.CharField(max_length=3,verbose_name="Sigla do Curso", unique=True,primary_key=True, auto_created=True)
    nomeCurso = models.CharField(max_length=200,verbose_name="Nome do Curso", null=False, blank=False, unique=True)
    descCurso = models.CharField(max_length=500,verbose_name="Descricao do Curso")
    
    def __str__(self):
            return self.siglaCurso
        
    class Meta:
        managed:False
        db_table = 'Curso'

       
class Disciplina(models.Model):
    idDisciplina = models.AutoField(verbose_name="id_disciplina", unique=True,primary_key=True, auto_created=True)
    nomeDisciplina = models.CharField(max_length=200,verbose_name="nome_disciplina", null=False, blank=False, unique=True)
    descDisciplina = models.CharField(max_length=500,verbose_name="desc_disciplina")
    
    siglaCurso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Sigla",blank=True)
    
    def __str__(self):
            return self.nomeDisciplina
        
    class Meta:
        managed:False
        db_table = 'Disciplina'

       
class Palavra_has_disciplina(models.Model):
   
    idPalavra = models.ForeignKey(Palavra, on_delete=models.CASCADE, verbose_name="Palavra")
    idDisciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina")
    
    def __str__(self):
            return self
        
    class Meta:
        managed:False
        db_table = 'Palavra_has_disciplina'