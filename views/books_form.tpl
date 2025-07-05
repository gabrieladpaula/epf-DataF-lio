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

        <div class="mb-3">
            <label class="form-label">Géneros:</label>
            <div>
                % for genero in generos:
                    <div class="form-check form-check-inline">
                        <input class="form-check-input" type="checkbox" name="generos" id="genero_{{genero['id']}}" value="{{genero['id']}}">
                        <label class="form-check-label" for="genero_{{genero['id']}}">
                            {{genero['nome']}}
                        </label>
                    </div>
                % end
            </div>
        </div>

        <button type="submit" class="btn btn-primary">Adicionar Livro</button>

    </form>
</div>