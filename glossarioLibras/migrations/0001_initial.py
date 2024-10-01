# Generated by Django 4.2.5 on 2023-11-23 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('siglaCurso', models.CharField(auto_created=True, max_length=3, primary_key=True, serialize=False, unique=True, verbose_name='Sigla do Curso')),
                ('nomeCurso', models.CharField(max_length=200, unique=True, verbose_name='Nome do Curso')),
                ('descCurso', models.CharField(max_length=500, verbose_name='Descricao do Curso')),
            ],
            options={
                'db_table': 'Curso',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('idDisciplina', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id_disciplina')),
                ('nomeDisciplina', models.CharField(max_length=200, unique=True, verbose_name='nome_disciplina')),
                ('descDisciplina', models.CharField(max_length=500, verbose_name='desc_disciplina')),
                ('siglaCurso', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='glossarioLibras.curso', verbose_name='Sigla')),
            ],
            options={
                'db_table': 'Disciplina',
            },
        ),
        migrations.CreateModel(
            name='Palavra',
            fields=[
                ('idPalavra', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='idPalavra')),
                ('nomePalavra', models.CharField(max_length=200, verbose_name='Palavra')),
                ('descPalavra', models.CharField(max_length=500, verbose_name='Descricao')),
            ],
            options={
                'db_table': 'Palavra',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='idUsuario')),
                ('loginUsuario', models.CharField(max_length=200, unique=True, verbose_name='Login')),
                ('senhaUsuario', models.CharField(max_length=200, verbose_name='Senha')),
                ('nomeUsuario', models.CharField(max_length=200, verbose_name='Nome Completo')),
                ('emailUsuario', models.EmailField(max_length=200, unique=True, verbose_name='Email')),
            ],
            options={
                'db_table': 'Usuario',
            },
        ),
        migrations.CreateModel(
            name='Sinal',
            fields=[
                ('idSinal', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='Id Sinal')),
                ('videoSinal', models.FileField(upload_to='uploads/videoSinal', verbose_name='Video')),
                ('descSinalTexto', models.CharField(max_length=500, verbose_name='Descricao Sinal em Texto')),
                ('descSinalImagem', models.ImageField(upload_to='uploads/imageSinal', verbose_name='Imagem')),
                ('nomePalavra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='palavra', to='glossarioLibras.palavra', verbose_name='Palavra referente')),
            ],
            options={
                'db_table': 'Sinal',
            },
        ),
        migrations.CreateModel(
            name='Palavra_has_disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDisciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glossarioLibras.disciplina', verbose_name='Disciplina')),
                ('idPalavra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glossarioLibras.palavra', verbose_name='Palavra')),
            ],
            options={
                'db_table': 'Palavra_has_disciplina',
            },
        ),
        migrations.AddField(
            model_name='palavra',
            name='loginUsuario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='glossarioLibras.usuario', verbose_name='Usuario responsavel'),
        ),
    ]
