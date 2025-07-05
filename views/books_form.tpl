%rebase('layout.tpl', title='Adicionar Novo Livro')

<div class="container">
    <h2>Adicionar Novo Livro</h2>
    <hr>

    <form action="/books/add" method="post">
        <div class="mb-3">
            <label for="title" class="form-label">Título:</label>
            <input type="text" class="form-control" name="title" id="title" required>
        </div>
        <div class="mb-3">
            <label for="author" class="form-label">Autor:</label>
            <input type="text" class="form-control" name="author" id="author" required>
        </div>
        
        <!-- Mais tarde, podemos adicionar aqui os campos para sinopse, upload de PDF e seleção de géneros -->
        
        <button type="submit" class="btn btn-primary">Adicionar Livro</button>
    </form>
</div>