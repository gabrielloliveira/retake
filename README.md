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
