% rebase('layout.tpl', title='Catálogo de Livros', current_user=current_user, pagina_class='pagina-catalogo')

<div class="pagina-catalogo">
    <div class="container with-navbar-offset">

        <!-- BARRA SUPERIOR -->
        <nav class="navbar-custom">
            <div class="navbar-container">
                <span class="logo">📘 <strong>DataFólio</strong></span>
                <div class="nav-links">
                    <a href="/login">Login</a>
                    <a href="/registo">Criar Conta</a>
                </div>
            </div>
        </nav>

        <!-- CABEÇALHO -->
        <div class="header-banner">
            <div class="icon">📚</div>
            <h1>Catálogo Digital</h1>
            <p>Explore nossa coleção organizada por categorias</p>
        </div>

        <!-- CAMPO DE BUSCA -->
        <form action="/catalogo" method="get" class="mb-4">
            <div class="search-bar">
                <input type="text" name="busca" placeholder="Procurar por título, autor ou categoria..." value="{{ termo_busca or '' }}">
                <button type="submit"><span>🔍</span></button>
            </div>
        </form>

        <!-- BOTÕES DE CATEGORIA -->
        <div class="filtros-genero">
            <button class="btn-genero ativo">Todas</button>
            <button class="btn-genero">Literatura Brasileira</button>
            <button class="btn-genero">Ficção Científica</button>
            <button class="btn-genero">Ciências Exatas</button>
            <button class="btn-genero">Ciências Humanas</button>
            <button class="btn-genero">Desenvolvimento Pessoal</button>
            <button class="btn-genero">Arte e Cultura</button>
        </div>

        <!-- RESULTADOS -->
        <div class="row">
            % if not books:
                <div class="col-md-12 empty-message">
                    <p>Nenhum livro encontrado.</p>
                </div>
            % else:
                % for book in books:
                    <!-- Aqui entra seu card -->
                % end
            % end
        </div>

    </div>
</div>
