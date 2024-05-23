# Django RESTful API #
API para gerenciar usuários, itens e pedidos.

## Índice
* Descrição
* Tecnologias
* Instalação
* Uso
* Rotas da API
* Contato

### Esta API foi desenvolvida usando Django REST Framework para gerenciar usuários, itens e pedidos. Ela fornece endpoints para criar, ler, atualizar e deletar (CRUD) usuários, itens e pedidos.



## Tecnologias
* Python 3.x
* Django 3.x
* Django REST Framework

## Instalação
Siga estas etapas para configurar o ambiente de desenvolvimento:

### - Clone o repositório:

* git clone [git@github.com/jrezsantos/Django-Rest-Api.git](https://github.com/jrezsantos/Django-Rest-Api.git)
* cd Django-Rest-Api

### - Crie um ambiente virtual e ative-o:
* python -m venv venv
* source env/bin/activate  # No Windows use `venv\Scripts\activate`


### - Instale as dependências:
pip install -r requirements.txt


### - Aplique as migrações do banco de dados:
python manage.py migrate
Crie um superusuário:
python manage.py createsuperuser


### - Inicie o servidor de desenvolvimento:
python manage.py runserver



### Uso
Após iniciar o servidor, você pode acessar a API através de http://127.0.0.1:8000/.



## Rotas da API
### Abaixo estão as principais rotas da API:

#### Usuários:

* GET /usuarios/ - Lista todos os usuários.
* POST /usuarios/ - Cria um novo usuário.
* GET /usuarios/{id}/ - Obtém detalhes de um usuário específico.
* PUT /usuarios/{id}/ - Atualiza um usuário específico.
* DELETE /usuarios/{id}/ - Deleta um usuário específico.

#### Itens:

* GET /itens/ - Lista todos os itens.
* POST /itens/ - Cria um novo item.
* GET /itens/{id}/ - Obtém detalhes de um item específico.
* PUT /itens/{id}/ - Atualiza um item específico.
* DELETE /itens/{id}/ - Deleta um item específico.

#### Pedidos:

* GET /pedidos/ - Lista todos os pedidos.
* POST /pedidos/ - Cria um novo pedido.
* GET /pedidos/{id}/ - Obtém detalhes de um pedido específico.
* PUT /pedidos/{id}/ - Atualiza um pedido específico.
* DELETE /api/pedidos/{id}/ - Deleta um pedido específico.


## Contato
Criado por juarezpsatosf@gmail.com  - sinta-se à vontade para me contatar!

Sinta-se à vontade para ajustar qualquer seção conforme necessário para se adequar às especificidades do seu projeto.





