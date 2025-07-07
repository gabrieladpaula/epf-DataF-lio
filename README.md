# Projeto Template: POO com Python + Bottle + JSON

Este é um projeto de template educacional voltado para o ensino de **Programação Orientada a Objetos (POO)** do Prof. Lucas Boaventura, Universidade de Brasília (UnB).

Utiliza o microframework **Bottle**. Ideal para uso em disciplinas introdutórias de Engenharia de Software ou Ciência da Computação.

## 💡 Objetivo

Fornecer uma base simples, extensível e didática para construção de aplicações web orientadas a objetos com aplicações WEB em Python, ideal para trabalhos finais ou exercícios práticos.

---

## 🗂 Estrutura de Pastas

```bash
poo-python-bottle-template/
├── app.py # Ponto de entrada do sistema
├── config.py # Configurações e caminhos do projeto
├── main.py # Inicialização da aplicação
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
├── controllers/ # Controladores e rotas
├── models/ # Definição das entidades (ex: User)
├── services/ # Lógica de persistência (JSON)
├── views/ # Arquivos HTML (Bottle Templating)
├── static/ # CSS, JS e imagens
├── data/ # Arquivos JSON de dados
└── .vscode/ # Configurações opcionais do VS Code
```


---

## 📁 Descrição das Pastas

### `controllers/`
Contém as classes responsáveis por lidar com as rotas da aplicação. Exemplos:
- `user_controller.py`: rotas para listagem, adição, edição e remoção de usuários.
- `base_controller.py`: classe base com utilitários comuns.
- __int__.py: arquivo que inicializa o módulo de controladores.

### `models/`
Define as classes que representam os dados da aplicação. Exemplo:
- pessoa.py: A classe base Pessoa, que criamos para aplicar o pilar da Herança. Ela contém os atributos e métodos comuns que podem ser herdados por outras classes, como a User.
-user.py: A classe User, que herda de Pessoa. Ela representa um usuário do sistema, encapsulando todos os seus dados, como id, nome, email, role, etc.
-livro.py: A classe Livro, que modela um livro do nosso acervo. Ela contém os atributos que definem um livro, como id, titulo, autor e sinopse.
-genero.py: A classe Genero, que representa um gênero literário. Ela define os atributos de um gênero, como id e nome.afo

### `services/`
Responsável por salvar, carregar e manipular dados usando arquivos JSON. Exemplo:
-auth_service.py: Controla a sessão do usuário e as permissões de acesso (@admin_required).
-genero_service.py: Busca a lista de todos os gêneros do banco de dados.
-livro_service.py: Executa todas as operações dos livros (CRUD, busca) e corrige a exibição de acentos.
-user_service.py: Gerencia os usuários: criação com senha segura (bcrypt), validação de login e listagem.


### `views/`
Contém os arquivos `.tpl` utilizados pelo Bottle como páginas HTML:
-layout.tpl: O template mestre que define a estrutura principal (cabeçalho, menu, rodapé) de --todas as outras páginas.
-catalogo.tpl: A vitrine do projeto. Exibe o catálogo público de livros, a barra de busca e -os links para os PDFs.
-login.tpl: Contém o formulário para que os usuários possam fazer o login.
-user_form.tpl: Contém o formulário para o registro de novos usuários na plataforma.
-admin_dashboard.tpl: A página inicial (dashboard) do painel do administrador.
-books.tpl: A tabela do painel de admin que lista todos os livros para gerenciamento.
-books_form.tpl: O formulário que o administrador usa para adicionar um novo livro.
-edit_book_form.tpl: O formulário que o administrador usa para editar um livro existente.
-user_list.tpl: A tabela específica do painel de admin que exibe a lista de todos os usuários -cadastrados.
-users.tpl: Template principal do dashboard do admin, que pode ser usado para listar informações gerais.
-visitor.tpl: Template para visitantes não logados, provavelmente a página inicial original do template.
-helper-final.tpl: Um template auxiliar, provavelmente vindo do material de exemplo do curso.


### `static/`
Arquivos estáticos como:
-css/: Contém as folhas de estilo que definem toda a aparência e o design do site.
     -style.css: O arquivo principal com toda a identidade visual do projeto (cores, fontes, layout).
     -helper.css: Um arquivo de estilos auxiliar, provavelmente do template original.
-img/: Pasta para guardar as imagens usadas no site.
     -BottleLogo.png: Imagem de exemplo do framework Bottle.
-pdfs/: A pasta onde os arquivos PDF dos livros são armazenados para que os usuários possam acessá-los através dos links no catálogo.

### `data/`
Armazena os arquivos `SQLite` que simulam o banco de dados:
-usuarios: Armazena os dados dos usuários cadastrados, incluindo nome, email, senha criptografada (bcrypt) e role (permissão de user ou admin).
-livros: Tabela principal que contém as informações de cada livro, como título, autor, sinopse e o caminho para o arquivo PDF ou link externo.
-generos: Uma lista de todos os gêneros literários disponíveis no sistema.
-livros_generos: Tabela de ligação que implementa a relação Muitos-para-Muitos, conectando um livro a múltiplos gêneros.
-historico_downloads: Estrutura para armazenar o histórico de quais usuários acessaram quais livros.

📘 Diagrama de Classes

![image](https://github.com/user-attachments/assets/852fcf9b-9e3a-4294-b959-82997ecc322b)




---

## ▶️ Como Executar

1. Crie o ambiente virtual na pasta fora do seu projeto:
```bash
python -m venv venv
venv\\Scripts\\activate     
```

2. Entre dentro do seu projeto criado a partir do template e instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a aplicação:
```bash
python main.py
```

4. Accese sua aplicação no navegador em: [http://localhost:8080](http://localhost:8080)

---

## ✍️ Personalização
Para adicionar novos modelos (ex: Atividades):

1. Crie a classe no diretório **models/**.

2. Crie o service correspondente para manipulação do JSON.

3. Crie o controller com as rotas.

4. Crie as views .tpl associadas.

---

## 🧠 Autor e Licença
Projeto desenvolvido como template didático para disciplinas de Programação Orientada a Objetos, baseado no [BMVC](https://github.com/hgmachine/bmvc_start_from_this).
Você pode reutilizar, modificar e compartilhar livremente.
