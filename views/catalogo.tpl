% rebase('layout.tpl', title='Catálogo de Livros', current_user=current_user)

<div class="container">
    <div class="row">
        <div class="col-md-12">
            <h1 class="mt-4">Catálogo de Livros</h1>
            <p class="lead">Explore nosso acervo completo.</p>
        </div>
    </div>

    <div class="row mb-4">
        <div class="col-md-12">
            <form action="/catalogo" method="get" class="form-inline">
                <div class="input-group w-100">
                    <input type="text" name="busca" class="form-control" placeholder="Buscar por título ou autor..." value="{{ termo_busca or '' }}">
                    <div class="input-group-append">
                        <button class="btn btn-primary" type="submit">Buscar</button>
                    </div>
                </div>
            </form>
        </div>
    </div>

    <div class="row">
        % if not books:
            <div class="col-md-12">
                <p>Nenhum livro encontrado.</p>
            </div>
        % else:
            % for book in books:
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="card h-100">
                        <a href="#">
                            <img class="card-img-top" src="https://via.placeholder.com/700x400" alt="Capa do Livro">
                        </a>
                        <div class="card-body">
                            <h4 class="card-title">
                                <a href="#">{{! book.get('titulo', 'Título Indisponível') }}</a>
                            </h4>
                            <h5>{{! book.get('autor', 'Autor Desconhecido') }}</h5>
                            <p class="card-text">
                                {{! book.get('sinopse', 'Sinopse não disponível.') }}
                            </p>
                            
                            <a href="{{! book.get('caminho_pdf', '#') }}" target="_blank" class="btn btn-success mt-2">
                                Acessar PDF
                            </a>
                            </div>
                    </div>
                </div>
            % end
        % end
    </div>
</div>