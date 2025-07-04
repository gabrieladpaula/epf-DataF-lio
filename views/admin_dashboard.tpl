%rebase('layout.tpl', title='Painel de Administração')

<div class="container">
    <h1>Painel de Administração</h1>
    <p>Bem-vindo(a) de volta, {{current_user['nome']}}!</p>
    <hr>

    <h2>Ações Rápidas</h2>
    <div class="actions">
        <a href="/books" class="btn purple">Gerir Livros</a>
        <a href="/books/add" class="btn purple">Adicionar Novo Livro</a>
        <a href="/users" class="btn">Gerir Utilizadores</a>
    </div>

    <h2 style="margin-top: 2rem;">Status do Sistema</h2>
    <div class="panel status">
        <ul>
            <li>Servidor <span class="status online">Online</span></li>
            <li>Database <span class="status connected">Conectado</span></li>
        </ul>
    </div>
</div>