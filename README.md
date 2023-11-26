**# To-Do Flask App**

Este projeto é um aplicativo básico de lista de tarefas desenvolvido como parte do curso de Desenvolvimento e Aplicações Web I. Utiliza o framework Flask para criar uma aplicação web simples que permite adicionar, editar e excluir tarefas.

## Estrutura do Projeto

### `app.py`

O arquivo `app.py` contém o código principal do aplicativo Flask. Aqui estão algumas funcionalidades principais:

- **Rotas:**
  - `/`: Página inicial que exibe a lista de tarefas.
  - `/add`: Rota para adicionar uma nova tarefa.
  - `/edit/<int:id>`: Rota para editar uma tarefa específica.
  - `/delete/<int:id>`: Rota para excluir uma tarefa específica.

- **Banco de Dados:**
  - Utiliza SQLite como banco de dados para armazenar as tarefas.
  - Cria uma tabela `tasks` com colunas `id` e `task`.

- **Paginação:**
  - Implementa a funcionalidade de paginação para exibir um número limitado de tarefas por página.

### `index.html` e `edit.html`

Esses arquivos contêm os templates HTML renderizados pelo Flask. `index.html` exibe a lista de tarefas, enquanto `edit.html` permite editar uma tarefa existente.

### `style.css`

O arquivo `style.css` fornece estilos simples para a apresentação visual do aplicativo.

## Funcionalidades Principais

- **Adição de Tarefas:** Os usuários podem adicionar novas tarefas através do formulário na página inicial.

- **Edição de Tarefas:** Clicando no botão "Edit" ao lado de uma tarefa, os usuários podem editar o conteúdo da tarefa.

- **Exclusão de Tarefas:** Clicando no botão "Delete" ao lado de uma tarefa, os usuários podem remover a tarefa.

- **Paginação:** A lista de tarefas é dividida em páginas para facilitar a navegação.

## Como Rodar o Projeto Localmente

1. Certifique-se de ter Python instalado.
2. Instale as dependências usando `pip install -r requirements.txt`.
3. Execute `python app.py` para iniciar o servidor Flask localmente.
4. Abra o navegador e acesse `http://localhost:5000`.

## Melhorias Futuras

- **Autenticação de Usuário:** Adicione autenticação para que cada usuário tenha sua própria lista de tarefas.

- **Notificações:** Implemente notificações para lembrar os usuários de suas tarefas pendentes.

- **Melhorias de Design:** Aprimore a aparência do aplicativo com estilos mais modernos e responsivos.

- **Comentários e Documentação:** Adicione comentários ao código e uma documentação mais abrangente.

Este projeto serve como uma introdução prática ao desenvolvimento web usando Flask e fornece uma base sólida para futuras expansões e melhorias.
