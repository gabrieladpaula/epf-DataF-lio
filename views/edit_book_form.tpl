%rebase('layout.tpl', title='Editar Livro')

<div class="container">
    <h2>Editar Livro: {{!book['titulo']}}</h2>
    <hr>

    <form action="/books/edit/{{book['id']}}" method="post">
        <div class="mb-3">
            <label for="title" class="form-label">Título:</label>
            <input type="text" class="form-control" name="title" id="title" value="{{!book['titulo']}}" required>
        </div>

        <div class="mb-3">
            <label for="author" class="form-label">Autor:</label>
            <input type="text" class="form-control" name="author" id="author" value="{{!book['autor']}}" required>
        </div>

        <div class="mb-3">
            <label for="sinopse" class="form-label">Sinopse:</label>
            <textarea class="form-control" name="sinopse" id="sinopse" rows="5">{{!book['sinopse']}}</textarea>
        </div>

        <div class="mb-3">
            <label for="caminho_pdf" class="form-label">Caminho do PDF:</label>
            <input type="text" class="form-control" name="caminho_pdf" id="caminho_pdf" value="{{!book['caminho_pdf']}}">
        </div>

        <div class="mb-3">
            <label class="form-label">Gêneros:</label>
            <div class="form-check">
                % for genero in generos:
                    <div class="form-check">
                        <input 
                            class="form-check-input" 
                            type="checkbox" 
                            name="generos" 
                            value="{{genero['id']}}"
                            id="genero_{{genero['id']}}"
                            % if genero['id'] in generos_atuais:
                                checked
                            % end
                        >
                        <label class="form-check-label" for="genero_{{genero['id']}}">
                            {{genero['nome']}}
                        </label>
                    </div>
                % end
            </div>
        </div>

        <button type="submit" class="btn btn-primary">Guardar Alterações</button>
    </form>
</div>
