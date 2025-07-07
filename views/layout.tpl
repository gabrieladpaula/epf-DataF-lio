<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DataFólio - {{title or 'Sistema'}}</title>
  <link rel="stylesheet" href="/static/css/style.css?v=3">
</head>
<body>

<header>
  % if current_user and current_user['role'] == 'admin':
    <span class="admin-badge">Administrador</span>
  % end

  <nav>
    % if current_user:
      <a href="/catalogo">Catálogo</a>
      <a href="/perfil">Meu Perfil</a>
      % if current_user['role'] == 'admin':
        <a href="/books/add">Adicionar Livro</a>
        <a href="/users">Gerenciar Usuários</a>
      % end
      <a href="/logout">Logout</a>
    % end
  </nav>
</header>

<body class="{{pagina_class or ''}}">
    %try:
    <main class="page-content {{pagina_class}}">
%except NameError:
    <main class="page-content">
%end
        {{!base}}
    </main>

<footer class="rodape">
  <p>&copy; 2025, DataFólio. Todos os direitos reservados.</p>
</footer>
%if not pagina_login and not pagina_cadastro:
    <footer class="rodape">
        © 2025, DataFólio. Todos os direitos reservados.
    </footer>
%end

</body>
</html>
