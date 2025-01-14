TaskMaster Pro
O TaskMaster Pro é um aplicativo em Python com interface gráfica desenvolvida para gerenciamento de tarefas. Ele permite criar, editar, remover e organizar tarefas, com a possibilidade de alterar seu status e salvar os dados em arquivos Excel para fácil portabilidade.

Funcionalidades
Adicione novas tarefas com um identificador único.
Editar tarefas existentes.
Remover tarefas com confirmação do usuário.
Alterar o status das tarefas (Pendente, Em Progresso, Concluído).
Salvar tarefas em um arquivo Excel padrão ( tasks.xlsx).
Exporte tarefas para outros locais usando "Salvar Como".
Tecnologias Utilizadas
Python : Linguagem principal do projeto.
Tkinter : Para construção da interface gráfica.
Pandas : Para manipulação e salvamento de dados.
OpenPyXL : Para suporte ao formato Excel.
Requisitos
Python 3.x instalado no sistema.
Biblioteca pandas e openpyxl instaladas:
bater

Copiar código
pip install pandas openpyxl
Como usar
Clonar este repositório:
bater

Copiar código
git clone https://github.com/seu-usuario/taskmaster-pro.git
Navegue até o diretório do projeto:
bater

Copiar código
cd taskmaster-pro
Execute o script principal:
bater

Copiar código
python app_tarefas.py
Interface
A interface gráfica inclui:

Campo para entrada de nome da tarefa.
Botões para adicionar, editar, remover e alterar status das tarefas.
Exibição de uma lista de tarefas organizadas por ID, nome e status.
Funcionalidade para salvar os dados no arquivo padrão ou exportar para um local personalizado.
Estrutura do Arquivo Excel
ID : Identificador único da tarefa.
Tarefa : Nome descritivo da tarefa.
Status : Estado atual da tarefa (Pendente, Em Progresso, Concluído).
Contribuições
Contribuições são bem-vindas! Caso tenha sugestões, encontre bugs ou deseje adicionar funcionalidades, abra um issue ou envie um pull request.
