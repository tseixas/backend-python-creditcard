Sumário
-----------------
<!--ts-->
- [backend-python-creditcard](#backend-python-creditcard)
- [Desafio técnico `Python`](#desafio-técnico-python)
  - [Alguns requisitos](#alguns-requisitos)
  - [Problema](#problema)
      - [IMPORTANTE:](#importante)
- [Instruções sobre desenvolvimento do projeto](#instruções-sobre-desenvolvimento-do-projeto)
  - [Tecnologias utilizadas](#tecnologias-utilizadas)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalando o projeto](#instalando-o-projeto)
  - [Autenticação](#autenticação)
  - [Testes](#testes)
<!--te-->
# backend-python-creditcard

Desafio para vaga de backend na MaisTodos

![portaldetodos](https://avatars0.githubusercontent.com/u/56608703?s=400&u=ae31a7a07d28895589b42ed0fcfc102c3d5bccff&v=4)

Desafio técnico `Python`
========================

Alguns requisitos
-----------------
  - Deixe o código em inglês;
  - Use Git;
  - Procure fazer `micro commits` que são muitos commits com menos código isso nos ajuda a compreender a sua lógica;
  - Pergunte nos sobre qualquer dúvida que venha a surgir durante o desenvolvimento;
  - Documente detalhadamente quaisquer referencias/ferramentas que vc pesquisar;
  - Crie um repositório público e nos passe o link para acompanharmos o desenvolvimento;
  - Faça testes automatizados (unitários e de integração);

Problema
--------

A `MAISTODOS LTDA` está lançando um sistema inovador de cadastros de cartões de crédito e precisa garantir toda a qualidade e padronização dos dados.
E esse sistema será uma `API` simples de cadastro de cartões de crédito, e o sistema irá receber no cadastro o seguinte payload:
```shell
{
    "exp_date": "02/2026",
    "holder": "Fulano",
    "number": "0000000000000001",
    "cvv": "123",
}
```

Como não é um cadastro qualquer, esses dados precisam passar por uma validação criteriosa e específica:

- **exp_date**
  - Ver se é uma data válida.
  - E se for válida, não pode ser menor do que a data de hoje. 😜
  - No banco de dados essa data deve ser gravada no formato yyyy-MM-[ultimo_dia_mes], por exemplo: 02/2022, deve ser 2022-02-28

- **holder**
  - Deve ser um campo obrigatório e deve possuir mais de 2 caracteres.

- **number**
  - Verificar se o número do cartão de crédito é válido, utilizando a lib https://github.com/MaisTodos/python-creditcard
  - Para instalar use ```pip install git+https://github.com/maistodos/python-creditcard.git@main```
  - Este campo deve ser gravado de forma criptografada no banco de dados.

- **cvv**
  - Este campo não é obrigatório, mas caso esteja presente no payload, deve possuir um tamanho entre 3 e 4 caracteres.
  - Este é um campo númerico.
  
#### IMPORTANTE: 
O modelo de dados que representa o cartao de crédito, deve possuir um campo chamado **brand** que representa a bandeira do cartão de crédito. Este campo deve ser preenchido de maneira automática, utilizando a mesma lib que foi usada para validar o número do cartão de crédito.

A api deve conter basicamente as urls (sugestão):
```shell
  GET  /api/v1/credit-card - listar os cartões de crédito
  GET  /api/v1/credit-card/`<key>` - detalhe do cartão de crédito
  POST /api/v1/credit-card - cadastrar um novo cartão de crédito
```

O acesso à api deve ser aberto ao mundo, porém deve possuir autenticação e autorização.

Você está livre para definir a melhor arquitetura e tecnologias para solucionar este desafio, todos os itens descritos nos campos são `sugestões`, mas não se esqueça de contar sua motivação no arquivo README que deve acompanhar sua solução, junto com os detalhes de como executar seu programa. Documentação e testes serão avaliados também =).

Nós solicitamos que você trabalhe no desenvolvimento desse sistema sozinho e não divulgue a solução desse problema pela internet.

Boa sorte, Equipe MaisTodos!

![Luck](https://media.giphy.com/media/l49JHz7kJvl6MCj3G/giphy.gif)

Instruções sobre desenvolvimento do projeto
========================

Tecnologias utilizadas
-----------------
Para esse projeto foram utilizadas as seguintes ferramentas no desenvolvimento.
- FastAPI
- PostgreSQL
- SQLAlchemy
- FastAPI-SQLAlchemy
- python-creditcard
- Docker e Docker compose

Ferramentas utilizadas nos testes:
- Pytest
- httpx

Pré-requisitos
-----------------
Para a construção e montagem desse projeto e visando a praticidade foram utilizados as tecnologias [docker](https://docs.docker.com/engine/install/) e [docker compose](https://docs.docker.com/compose/install/). 

Instalando o projeto
-----------------
- Clone o projeto com o comando ```git clone git@github.com:tseixas/backend-python-creditcard.git```

- Na raiz do projeto e já tendo configurado os itens mencionados no tópico de pré-requisitos, rodar os seguintes comandos no seu terminal.
1) ```make psql-up``` - comando irá montar e configurar um container docker com o banco de dados e a aplicação.

2) ```make start``` - comando irá subir o servidor da aplicação.

A aplicação ficará disponível via swagger na seguinte url http://127.0.0.1:8000/docs#/

> *OBS*: **make psql-down** - comando para remover o container da aplicação

Autenticação
-----------------
Para a utilização dos endpoints será necessário se autenticar, segue abaixo como realizar esse procedimento.

Foi desenvolvido duas formas de autenticação a primeira via swagger e a segunda via endpoint.

Abaixo segue passo-a-passo para os testes via swagger.
- Com o projeto já rodando, acesse a url http://127.0.0.1:8000/docs#/
- No canto superior direito haverá um botão chamado **Authorize**, clique nele e abrirá um modal.
- Preencha as informações de *username* e *password* com as informações abaixo.

  `username: admin`

  `password: secret`

- Após preenchido, confirme no botão **Authorize**
- Pronto! agora poderá acessar os endpoint até então protegidos.


Testes
-----------------
Foram realizados alguns testes e é possível executá-los da seguinte forma.

- No terminal de sua preferência e na raiz do projeto rodar o seguinte comando: ```pytest```
