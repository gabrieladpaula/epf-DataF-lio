% rebase('layout', title='Adicionar Livro')

<section class="form-section">
    <h1>Adicionar Livro</h1>

    <form action="{{action}}" method="post">
        <label for="title">Título:</label>
        <input type="text" name="title" id="title" required>

        <label for="author">Autor:</label>
        <input type="text" name="author" id="author" required>

        <label for="genre">Gênero:</label>
        <input type="text" name="genre" id="genre" required>

        <button type="submit" class="btn">Salvar</button>
    </form>
</section>
