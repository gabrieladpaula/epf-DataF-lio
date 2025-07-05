%rebase('layout.tpl', title='Editar Livro')

<div class="container">
    <h2>Editar Livro: {{book['titulo']}}</h2>
    <hr>

    <form action="/books/edit/{{book['id']}}" method="post">
        <div class="mb-3">
            <label for="title" class="form-label">Título:</label>
            <input type="text" class="form-control" name="title" id="title" value="{{book['titulo']}}" required>
        </div>
        <div class="mb-3">
            <label for="author" class="form-label">Autor:</label>
            <input type="text" class="form-control" name="author" id="author" value="{{book['autor']}}" required>
        </div>
        <div class="mb-3">
            <label for="sinopse" class="form-label">Sinopse:</label>
            <textarea class="form-control" name="sinopse" id="sinopse" rows="5">{{book['sinopse']}}</textarea>
        </div>

        <button type="submit" class="btn btn-primary">Guardar Alterações</button>
    </form>
</div>