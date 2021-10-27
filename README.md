# Retake

Projeto feito para o desafio backend retake

### Dependências

- Python >= 3.6
- Docker

### Como rodar

- Clone o projeto: ```git clone git@github.com:gabrielloliveira/retake.git```

Para rodar o projeto, você precisa setar um arquivo .env no projeto. Para fazer isso, você tem que instalar 
as dependências e rodar o arquivo gerador de .env.

- Criar um virtualenv: ```python -m venv env```
- Instalar as dependências: ```pip install -r requirements.txt```
- Gerar o arquivo .env: ```python contrib/generate_env.py```

Não é necessário instalar o virtualenv dentro da máquina local. Porém, caso isso não seja feito,
você deverá criar manualmente um arquivo .env com as seguintes chaves: SECRET_KEY, ALLOWED_HOSTS e DEBUG

Agora com tudo configurado, você pode rodar o projeto usando o docker:
- ```docker-compose up --build```

Você poderá acessar o projeto rodando em ```http://localhost:8000```

### Como acessar o admin da aplicação

Para acessar o django admin, você deve criar um usuário no BD do projeto django.
Para isso, devemos dizer para o docker que rode o comando de ciração de usuário. Fazemos isso com:

- ```docker-compose exec web python manage.py createsuperuser```

A partir daí, você informa seu login e senha. Após isso, você terá acesso ao projeto web.


### E se eu quiser rodar sem usar o docker?

Para rodar fora dos containers docker, você precisa fazer 2 coisas:

- Instalar o redis-cli no seu computador.
- Trocar, no arquivo ```retake/celery.py```, a URL do BROKER da aplicação. Geralmente, em ambiente local, é o 
```redis://localhost```
