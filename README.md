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
```
Ver informações
```
/usuarios/crud-contratante/<slug_do_usuário>/ --> Método GET
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
```
Deletar
```
/usuarios/crud-contratante/<slug_do_usuário>/ --> Método DELETE
```
## Usuário Fornecedor Buffer
Criar
```
/usuarios/crud-fornecedor-buffer/ --> Método POST
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
/usuarios/crud-fornecedor-buffer/<slug_do_usuário>/ --> Método GET
```
Editar
```
/usuarios/crud-fornecedor-buffer/<slug_do_usuário>/ --> Método PUT
itens no json:
- nome (String)
- email (String)
- telefone (String)
- cpf_cnpj (String)
- endereco (String)
- faz_entrega (boolean)
```
Deletar
```
/usuarios/crud-fornecedor-buffer/<slug_do_usuário>/ --> Método DELETE
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
```
Ver informações
```
/eventos/crud-eventos/<slug_do_evento>/ --> Método GET
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
```
Deletar
```
/eventos/crud-eventos/<slug_do_evento>/ --> Método DELETE
```
Listar eventos criados pelo usuário
```
/eventos/crud-eventos/list-owner-eventos/ --> Método GET
```
## Itens
Criar
```
/pacotes/crud-itens/ --> Método POST
itens no json:
- nome (String)
```
Ver informações
```
/pacotes/crud-itens/<slug_do_evento>/ --> Método GET
```
Editar
```
/pacotes/crud-itens/<slug_do_evento>/ --> Método PUT
itens no json:
- nome (String)
```
Deletar
```
/pacotes/crud-itens/<slug_do_evento>/ --> Método DELETE
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
```
Ver informações
```
/pacotes/crud-pacotes/<slug_do_evento>/ --> Método GET
```
Editar
```
/pacotes/crud-pacotes/<slug_do_evento>/ --> Método PUT
itens no json:
- nome (String)
- quantidade_pessoas (int)
- restricoes (Apenas as Strings 'Vegetariano' ou 'Regional')
- preco (float)
```
Deletar
```
/pacotes/crud-pacotes/<slug_do_evento>/ --> Método DELETE
```
## Item do Pacote
Colocar item no pacote
```
/pacotes/crud-item-pacote/<slug_do_pacote>/ --> Método POST
itens no json:
- item (int -> id do item)
- quantidade_item (int)
```
Ver itens do pacote
```
/pacotes/crud-item-pacote/<slug_do_pacote>/ --> Método GET
```
Editar item de um pacote
```
/pacotes/crud-item-pacote/<slug_do_pacote>/<slug_do_item_pacote>/ --> Método PUT
itens no json:
- item (int -> id do item)
- quantidade_item (int)
```
Deletar
```
/pacotes/crud-item-pacote/<slug_do_pacote>/<slug_do_item_pacote>/ --> Método DELETE
```
