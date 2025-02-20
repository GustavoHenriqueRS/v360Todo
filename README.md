# V360Todo

V360Todo é uma aplicação simples para gerenciamento de listas de tarefas, desenvolvida com Django e Tailwind CSS.

## Visão Geral

A aplicação permite que o usuário se identifique pelo e-mail e crie, visualize, edite e exclua listas de tarefas, bem como os itens dentro dessas listas. O design é responsivo e moderno, utilizando Tailwind CSS para a estilização.

## Links

- **Repositório:** [https://github.com/GustavoHenriqueRS/v360Todo](https://github.com/GustavoHenriqueRS/v360Todo)
- **Deploy:** [https://v360todo-060e5e9bd337.herokuapp.com/](https://v360todo-060e5e9bd337.herokuapp.com/)

## Funcionalidades

- Cadastro e autenticação simples via e-mail.
- Criação, edição e exclusão de listas de tarefas.
- Adição, edição e remoção de itens dentro de uma lista.
- Interface moderna e responsiva com Tailwind CSS.

## Instalação e Execução Local

### Pré-requisitos

- Python 3.x
- Node.js e npm (necessários para compilar o CSS do Tailwind)
- Virtualenv (opcional, mas recomendado)

### Passos para Rodar a Aplicação Localmente

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/GustavoHenriqueRS/v360Todo.git
   cd v360Todo
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Instale as dependências Python:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o Tailwind CSS:**

   - Navegue até o diretório onde está o Tailwind (`theme/static_src`):

     ```bash
     cd theme/static_src
     npm install
     ```

   - Compile os arquivos do Tailwind:

     ```bash
     npm run build
     ```
     
     **Ou** para desenvolvimento use:
     
     ```bash
     cd ../../
     python manage.py tailwind start
     ```
     
5. **Aplique as migrações e gere os arquivos estáticos:**

   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

6. **Inicie o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação:**

   Abra o navegador e acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Deploy

A aplicação está configurada para deploy no Heroku. Certifique-se de que os arquivos do Django (como `manage.py` e `requirements.txt`) estão na raiz do repositório para que o buildpack Python funcione corretamente.  
Durante o deploy, se necessário, o comando de build do Tailwind é executado para compilar os assets e o comando `collectstatic` coleta os arquivos estáticos.

Caso ocorra algum problema com os assets estáticos, verifique a documentação do Heroku para aplicações Django: [Django Assets on Heroku](https://devcenter.heroku.com/articles/django-assets).

## Contribuição

Contribuições, sugestões e feedback são bem-vindos! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
