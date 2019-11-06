# Prova EBI

### Aplicações desenvolvidas como parte da seleção de estagiário para a EBI Informática.

Abaixo contém as três partes da prova com suas respectivas aplicações e instruções de uso:

- [Parte 1](https://github.com/LeonardoFurtado/prova-ebi/blob/master/README.md#parte-1): Use a biblioteca requests para consumir api da receitaws com o método GET  e exiba no console os seguintes campos:

  - atividade_principal
  - atividades_secundarias
  - nome
  - uf
  - telefone
  - email
  - data de abertura

- [Parte 2](https://github.com/LeonardoFurtado/prova-ebi/blob/master/README.md#parte-2) : 
Utilize a biblioteca React.js ( https://pt-br.reactjs.org/ ) para criar uma interface simples que efetue as mesmas tarefas da Parte 1, através de um navegador web. É necessário informar ao usuário caso o CNPJ seja inválido.

- [Parte 3](https://github.com/LeonardoFurtado/prova-ebi/blob/master/README.md#parte-3) : 
Desenvolva um CRUD seguindo a sua modelagem, as perguntas a serem respondidas são:

- Quais são as empresas cadastradas?
- Quais serviços uma empresa disponibiliza? 
- Quais prestações de serviço foram feitas por uma dada empresa?


Observações:

- Poderemos usar os campos da entidade empresa para realizar a pesquisa.
- O banco de dados deve pode ser em sqlite, mas fica a seu critério
- Fica ao seu critério usar ORM ou não.
- O avaliador deve ter alguma forma fácil de usar o seu CRUD.
- Cadastro automático de empresa no banco será bem vindo.
- O seu software deve conter um passo a passo de como executá-lo numa máquina linux.


#### Parte 1

Use a biblioteca requests para consumir api da receitaws com o método GET

#### Parte 2


A resolução desta parte está no seguinte repositorio: ![receitaws-react](https://github.com/LeonardoFurtado/receitaws-react)

#### Parte 3


Clone ou faça download deste repositório.

Na pasta do repositório execute:
- `pip3 install -r requirements.txt` Para instalar as dependências do projeto.
- `python3 manage.py runserver` para executar a aplicação.

