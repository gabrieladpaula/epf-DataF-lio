<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DataFólio - {{title or 'Sistema'}}</title>
    <link rel="stylesheet" href="/static/css/style.css?v=2">

</head>
<body>

  <header>
    <div class="header-left">
        <div class="logo">DataFólio</div>
        <span class="admin-badge">Administrador</span>
    </div>
    <nav>
        <a href="/users">Usuários</a>
        <a href="/users/add">Adicionar Usuário</a>
        <a href="/books/add">Adicionar Livro</a>
    </nav>
</header>


    <main class="container">
        {{!base}}
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2025, DataFólio. Todos os direitos reservados.</p>
        </div>
    </footer>

</body>
</html>
