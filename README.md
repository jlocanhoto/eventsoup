# Eventsoup
> Bem vindo ao repositório principal do Eventsoup, plataforma para facilitar a organização de eventos, unindo os realizadores de evento aos fornecedores dos mais diversos serviços.

## Configurando e rodando o projeto.
*  _clone o repositório no seu computador:_
```sh
git clone https://github.com/marcelsan/eventsoup-backend.git
```
* Em seguida crie um ambiente virtual na sua máquina para comportar todas as libs requeridas para o funcionamento correto da aplicação:
> Usaremos python 3 no nosso projeto.
```sh
virtualenv -p python3 env
```
* Após criado o ambiente virtual, execute o seguinte comando para ativar o ambiente virtual:
```sh
$ source env/bin/activate
```
> Em seguida você vai notar que seu terminal agora contem um '(env)' antes do diretório corrente.
* Agora que estamos no nosso ambiente virtual, vamos instalar todas as dependencias, mas primeiro precisamos ir até o diretório raiz do nosso projeto, que contem o arquivo 'requirements.txt':
```sh
$ ls
eventsoup README.md requirements.txt
$ pip install -r requirements.txt
```
* Após instalado todos as dependencias, agora vamos criar um arquivo de configurações para o banco de dados local:
> No diretorio do arquivo settings.py, deve-se criar um arquivo com o nome local_settings.py
> Dentro do arquivo deve ser colocado o seguinte código:
```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

* Após instalar todas as dependencias, agora vamos rodar nosso projeto:
> no mesmo diretório e com a env ativada, vamos entrar na pasta 'eventsoup' que contem o arquivo '[manage.py](https://docs.djangoproject.com/en/1.11/ref/django-admin/)' e rodar o projeto na porta 8080:
```sh
$ python manage.py runserver 8080
```

* Voila!, se tudo deu certo, você verá a seguinte mensagem:
```
Django version 1.11.1, using settings 'eventsoup.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CONTROL-C.
```

* Basta acessar o link 'http://127.0.0.1:8080/' e mãos à obra!

# Requirements
```
Django==1.11.1
djangorestframework==3.6.3
Markdown==2.6.8
pytz==2017.2
```

# Rotas

## URL do servidor
```
https://eventsoup-backend.herokuapp.com/
```

## Login

Fazer login na plataforma e receber um token para fazer as outras requisições
```
/api-token-auth/ --> Método POST
itens no json:
- cpf_cnpj (String)
- password (String)

Resposta:
- token (String)
```
Este token deve ser guardado para ser utilizado nas demais requisições à aplicação

## Usuário Contratante
Criar
```
/usuarios/crud-contratante/ --> Método POST
itens no json:
- nome (String)
- email (String)
- telefone (String)
- cpf_cnpj (String)
- endereco (String)
- password1 (String)
- password2 (String)

conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Ver informações
```
/usuarios/crud-contratante/<slug_do_usuário>/ --> Método GET
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Editar
```
/usuarios/crud-contratante/<slug_do_usuário>/ --> Método PUT
itens no json:
- nome (String)
- email (String)
- telefone (String)
- cpf_cnpj (String)
- endereco (String)
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Deletar
```
/usuarios/crud-contratante/<slug_do_usuário>/ --> Método DELETE
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
## Usuário Fornecedor Buffer
Criar
```
/usuarios/crud-fornecedor-buffet/ --> Método POST
itens no json:
- nome (String)
- email (String)
- telefone (String)
- cpf_cnpj (String)
- endereco (String)
- faz_entrega (boolean)
- password1 (String)
- password2 (String)
```
Ver informações
```
/usuarios/crud-fornecedor-buffet/<slug_do_usuário>/ --> Método GET
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Editar
```
/usuarios/crud-fornecedor-buffet/<slug_do_usuário>/ --> Método PUT
itens no json:
- nome (String)
- email (String)
- telefone (String)
- cpf_cnpj (String)
- endereco (String)
- faz_entrega (boolean)

conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Deletar
```
/usuarios/crud-fornecedor-buffet/<slug_do_usuário>/ --> Método DELETE
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```

## Evento
Criar
```
/eventos/crud-eventos/ --> Método POST
itens no json:
- nome (String)
- quantidade_pessoas (int)
- data (String)
- local (String)
- restricoes (Apenas as Strings 'Vegetariano' ou 'Regional')
- orcamento (float)

conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Ver informações
```
/eventos/crud-eventos/<slug_do_evento>/ --> Método GET
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Editar
```
/eventos/crud-eventos/<slug_do_evento>/ --> Método PUT
itens no json:
- nome (String)
- quantidade_pessoas (int)
- data (String)
- local (String)
- restricoes (Apenas as Strings 'Vegetariano' ou 'Regional')
- orcamento (float)

conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Deletar
```
/eventos/crud-eventos/<slug_do_evento>/ --> Método DELETE
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Listar eventos criados pelo usuário
```
/eventos/crud-eventos/list-owner-eventos/ --> Método GET
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
## Itens
Criar
```
/pacotes/crud-itens/ --> Método POST
itens no json:
- nome (String)

conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Ver informações
```
/pacotes/crud-itens/<slug_do_evento>/ --> Método GET
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Editar
```
/pacotes/crud-itens/<slug_do_evento>/ --> Método PUT
itens no json:
- nome (String)

conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Deletar
```
/pacotes/crud-itens/<slug_do_evento>/ --> Método DELETE
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
## Pacote
Criar
```
/pacotes/crud-pacotes/ --> Método POST
itens no json:
- nome (String)
- quantidade_pessoas (int)
- restricoes (Apenas as Strings 'Vegetariano' ou 'Regional')
- preco (float)

conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Ver informações
```
/pacotes/crud-pacotes/<slug_do_evento>/ --> Método GET
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Editar
```
/pacotes/crud-pacotes/<slug_do_evento>/ --> Método PUT
itens no json:
- nome (String)
- quantidade_pessoas (int)
- restricoes (Apenas as Strings 'Vegetariano' ou 'Regional')
- preco (float)

conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Deletar
```
/pacotes/crud-pacotes/<slug_do_evento>/ --> Método DELETE
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
## Item do Pacote
Colocar item no pacote
```
/pacotes/crud-item-pacote/<slug_do_pacote>/ --> Método POST
itens no json:
- item (int -> id do item)
- quantidade_item (int)

conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Ver itens do pacote
```
/pacotes/crud-item-pacote/<slug_do_pacote>/ --> Método GET
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Editar item de um pacote
```
/pacotes/crud-item-pacote/<slug_do_pacote>/<slug_do_item_pacote>/ --> Método PUT
itens no json:
- item (int -> id do item)
- quantidade_item (int)

conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```
Deletar
```
/pacotes/crud-item-pacote/<slug_do_pacote>/<slug_do_item_pacote>/ --> Método DELETE
conteudo de autorização:
- Authorization (String)
a string de autorização deve começar com "JWT" seguido de espaço e o token recibido no login
```