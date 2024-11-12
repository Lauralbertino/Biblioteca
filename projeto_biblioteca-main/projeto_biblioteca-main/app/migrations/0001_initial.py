# Generated by Django 5.1.3 on 2024-11-12 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='--', help_text='Informe o nome da cidade', max_length=255, unique=True, verbose_name='Nome da Cidade')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='--', help_text='Informe o nome do gênero literário', max_length=255, unique=True, verbose_name='Nome do Gênero')),
            ],
            options={
                'verbose_name': 'Gênero',
                'verbose_name_plural': 'Gêneros',
            },
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(default='--', help_text='Informe a sigla da Unidade Federativa', max_length=2, unique=True, verbose_name='Sigla')),
            ],
            options={
                'verbose_name': 'Unidade Federal',
                'verbose_name_plural': 'Unidades Federais',
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='--', help_text='Informe o nome', max_length=255, verbose_name='Nome')),
                ('email', models.CharField(default='--', help_text='Informe o e-mail', max_length=255, verbose_name='E-mail')),
                ('telefone', models.CharField(default='--', help_text='Informe o telefone', max_length=20, verbose_name='Telefone')),
                ('cpf', models.CharField(default='--', help_text='Informe o CPF', max_length=11, verbose_name='CPF')),
                ('data_nasc', models.DateField(default='2000-01-01', help_text='Informe a data de nascimento', verbose_name='Data de Nascimento')),
                ('cidade', models.ForeignKey(default=1, help_text='Selecione a cidade', on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='--', help_text='Informe o nome', max_length=255, verbose_name='Nome')),
                ('email', models.CharField(default='--', help_text='Informe o e-mail', max_length=255, verbose_name='E-mail')),
                ('telefone', models.CharField(default='--', help_text='Informe o telefone', max_length=20, verbose_name='Telefone')),
                ('cnpj', models.CharField(default='--', help_text='Informe o CNPJ', max_length=14, verbose_name='CNPJ')),
                ('razao_social', models.CharField(default='--', help_text='Informe a razão social', max_length=255, verbose_name='Razão Social')),
                ('data_fund', models.DateField(default='2000-01-01', help_text='Informe a data de fundação', verbose_name='Data de Fundação')),
                ('cidade', models.ForeignKey(default=1, help_text='Selecione a cidade', on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Editora',
                'verbose_name_plural': 'Editoras',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='--', help_text='Informe o nome do livro', max_length=255, verbose_name='Nome do Livro')),
                ('preco', models.IntegerField(default=0, help_text='Informe o preço do livro', verbose_name='Preço')),
                ('data_pub', models.DateField(default='2000-01-01', help_text='Informe a data de publicação', verbose_name='Data de Publicação')),
                ('autor', models.ForeignKey(default=1, help_text='Selecione o autor', on_delete=django.db.models.deletion.CASCADE, to='app.autor', verbose_name='Autor')),
                ('editora', models.ForeignKey(default=1, help_text='Selecione a editora', on_delete=django.db.models.deletion.CASCADE, to='app.editora', verbose_name='Editora')),
                ('genero', models.ForeignKey(default=1, help_text='Selecione o gênero literário', on_delete=django.db.models.deletion.CASCADE, to='app.genero', verbose_name='Gênero Literário')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(default=1, help_text='Selecione a Unidade Federal', on_delete=django.db.models.deletion.CASCADE, to='app.uf', verbose_name='Unidade Federal'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='--', help_text='Informe o nome', max_length=255, verbose_name='Nome')),
                ('email', models.CharField(default='--', help_text='Informe o e-mail', max_length=255, verbose_name='E-mail')),
                ('telefone', models.CharField(default='--', help_text='Informe o telefone', max_length=20, verbose_name='Telefone')),
                ('cpf', models.CharField(default='--', help_text='Informe o CPF', max_length=11, verbose_name='CPF')),
                ('data_nasc', models.DateField(default='2000-01-01', help_text='Informe a data de nascimento', verbose_name='Data de Nascimento')),
                ('cidade', models.ForeignKey(default=1, help_text='Selecione a cidade', on_delete=django.db.models.deletion.CASCADE, to='app.cidade', verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ent', models.DateField(default='2000-01-01', help_text='Informe a data de entrega', verbose_name='Data de Entrega')),
                ('data_sai', models.DateField(default='2000-01-01', help_text='Informe a data de saída', verbose_name='Data de Saída')),
                ('livro', models.ForeignKey(default=1, help_text='Selecione o livro', on_delete=django.db.models.deletion.CASCADE, to='app.livro', verbose_name='Livro')),
                ('usuario', models.ForeignKey(default=1, help_text='Selecione o usuário', on_delete=django.db.models.deletion.CASCADE, to='app.usuario', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Empréstimo',
                'verbose_name_plural': 'Empréstimos',
            },
        ),
    ]