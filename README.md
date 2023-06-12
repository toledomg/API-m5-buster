# M5 - Kenzie Buster - Sprint 4

## Introdução

- Você foi selecionado pelo gestor da sua empresa para desenvolver uma API com o intuito de fazer uma gestão de vendas de filmes que está querendo sair do papel e caneta e planilhas bagunçadas. Nesse projeto você criará uma aplicação para gerenciar usuários, filmes e compras, incluindo autenticação e permissões de rotas para diferentes tipos de usuário.

## Requisitos

- Configurar a estrutura do projeto, incluindo .gitignore, venv, requirements.txt;

- Customizar usuário com base no AbstractUser;

- Registrar models no Django Admin;

- Serializers convencionais;

- Validação customizada;

- Sobrescrita de métodos de serializers;

- Proteção de rotas via autenticação JWT e permissão customizada do Django Rest Framework;

- Tabela Pivô customizada;

- Campos de escolha para atributos de model;

- Paginação com APIView;

### Entregáveis

Link deste repositório no GitHub;

- [Github Repo](https://github.com/toledomg/m5-kenzie-buster-sp-4-toledomg)

Link do repositório do GitHub, forkado deste template.

- [Github Template](https://github.com/Kenzie-Academy-Brasil-Developers/m5-kenzie-buster)

##

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:

```shell
pip list
```

- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:

```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:

```bash
python -m venv venv
```

2. Ative seu venv:

```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate

# git bash:
source venv/Scripts/activate
```

3. Instale o pacote `pytest-testdox`:

```shell
pip install pytest-testdox pytest-django
```

5. Vá até o arquivo `pytest.ini` e modifique o nome do projeto `my_project_name.settings` para o nome do **seu_projeto**.settings (onde se encontra o settings.py)

6. Agora é só rodar os testes no diretório principal do projeto:

```shell
pytest --testdox -vvs
```

## Rodando os testes de cada tarefa isoladamente

Ao fim de cada tarefa será possível executar uma suite de testes direcionada àquela tarefa específica. Lembre-se de sempre estar com o **virtual enviroment (venv) ativado**.

- Rodando testes da Tarefa 1:

```python
pytest --testdox -vvs tests/tarefas/t1/
```

- Rodando testes da Tarefa 2:

```python
pytest --testdox -vvs tests/tarefas/t2/
```

- Rodando testes da Tarefa 3:

```python
pytest --testdox -vvs tests/tarefas/t3/
```

- Rodando testes da Tarefa 4:

```python
pytest --testdox -vvs tests/tarefas/t4/
```

## Comandos Úteis

Abrir Shell nativo Django

```shell
python manage.py shell
```

Instalar Django

```shell
pip install django
```

Instalar Django Rest Framework

```shell
pip install djangorestframework
```

Inicializar Projeto Django

```shell
django-admin startproject nome_do_projeto
```

Inicializar App Django

```shell
python manage.py startapp nome_do_app
```

Salvar requirements

```shell
pip freeze > requirements.txt
```

Instalar requirements

```shell
pip install -r requirements.txt
```

Criar Migrations

```shell
python manage.py makemigrations
```

Rodar Migrations

```shell
python manage.py migrate
```

Server Start

```shell
python manage.py runserver
```
