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

