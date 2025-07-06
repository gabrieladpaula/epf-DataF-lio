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
        
        %if current_user and current_user['role'] == 'admin':
            <span class="admin-badge">Administrador</span>
        %end
    </div>

    <nav>
        %if current_user:
            %# --- MENU PARA UTILIZADOR LOGADO ---
            <a href="/catalogo">Catalogo</a>
            <a href="/perfil">Meu Perfil</a>
            
            %# Mostra os links de admin apenas se o utilizador for um admin
            %if current_user['role'] == 'admin':
                <a href="/books/add">Adicionar Livro</a>
                <a href="/users">Gerenciar Usuários</a>
                <a href="/books/add">Adicionar Livro</a>
            %end

            <a href="/logout">Logout</a>
        %else:
            %# --- MENU PARA VISITANTE ---
            <a href="/login">Login</a>
            <a href="/users/add">Registo</a>
        %end
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