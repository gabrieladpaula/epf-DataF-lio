<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Livros</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>

<header>
    <div class="logo">DataFólio 📚</div>
    <nav>
        <a href="/books">Livros</a>
        <a href="/books/add">Adicionar Livro</a>
        <a href="/users">Usuários</a>
        <a href="/">Dashboard</a>
    </nav>
</header>

<main>
    <h1>📚 Lista de Livros</h1>

    <a href="/books/add" class="btn">+ Adicionar Livro</a>

    <table>
        <tr>
            <th>ID</th>
            <th>Título</th>
            <th>Autor</th>
            <th>Ações</th>
        </tr>
        % for book in books:
        <tr>
            <td>{{book["id"]}}</td>
            <td>{{book["titulo"]}}</td>
            <td>{{book["autor"]}}</td>
            <td class="actions">
                <a href="/books/edit/{{book['id']}}" class="btn btn-sm btn-edit">Editar</a>
                <form action="/books/delete/{{book['id']}}" method="post" style="display:inline;">
                    <button type="submit" class="btn btn-sm btn-danger">Apagar</button>
                </form>
            </td>
        </tr>
        % end
    </table>
</main>

</body>
</html>