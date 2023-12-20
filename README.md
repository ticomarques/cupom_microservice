# MVP 2 - CUPOM MICROSERVICE (Backend) - Engenharia de Software PUC-Rio (2023.3)

Microsserviço para gerenciamento de cupom, um CRUD de cupom.

---


# Backend tecnologias

O backend deste projeto foi desenvolido em Python com SQL Alchemy. Todas as dependencias podem ser consultadas no arquivo requirements.



## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

1- Criar
2- Ativar
3- Desativar

Como criar um virtal env:
```
python3 -m venv env 
```

Como ativar um virtal env:
```
source env/bin/activate 
```

Como desativar um virtal env:
```
deactivate 
```

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 8000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 8000 --reload
```

Abra o [http://localhost:8000/#/](http://localhost:8000/#/) no navegador para verificar o status da API em execução.

## Docker
## Como executar 

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.

```
$ docker build -t cupom .
```
Obs: Cupom será o nome dado a imagem.

Uma vez criada a imagem, para executar o container basta executar o seguinte o comando:

```
$ docker run -p 8000:8000 cupom
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:8000/#/](http://localhost:8000/#/) no navegador.
