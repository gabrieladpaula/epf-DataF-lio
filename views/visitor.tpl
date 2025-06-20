%rebase('layout', title='Acesso Visitante')

<section class="visitor-section">
    <div class="visitor-header">
        <h1>📖 Acesso Visitante</h1>
        <p>Explore nossa biblioteca digital - Visualização limitada</p>

        <div class="alert">
            ⚠️ <strong>Acesso Limitado:</strong> Como visitante, você pode navegar e visualizar informações dos livros, mas não pode fazer downloads. 
            <br><strong>Faça login para ter acesso completo!</strong>
        </div>
    </div>

    <div class="stats">
        <div class="card">
            <h3>Downloads</h3>
            <p class="blocked">🔒 Bloqueado</p>
        </div>
        <div class="card">
            <h3>Livros Disponíveis</h3>
            <p>{{len(books)}}</p>
        </div>
        <div class="card">
            <h3>Status</h3>
            <p class="status-visitante">🟡 Visitante</p>
        </div>
    </div>

    <div class="search-filter">
        <input type="text" placeholder="🔍 Procurar por título ou autor...">
        <select>
            <option>Todos</option>
            <option>Romance</option>
            <option>Ficção</option>
            <option>Clássico</option>
            <option>Filosofia</option>
            <option>Distopia</option>
            <option>Aventura</option>
        </select>
    </div>

    <div class="books-grid">
        % for book in books:
            <div class="book-card">
                <img src="/static/img/{{book['image']}}" alt="{{book['title']}}">
                <h4>{{book['title']}}</h4>
                <p>{{book['author']}}</p>
                <div class="tags">
                    % for tag in book['tags']:
                        <span class="tag">{{tag}}</span>
                    % end
                </div>
                <div class="locked-badge">🔒 Bloqueado</div>
            </div>
        % end
    </div>
</section>

<section class="unlock-section">
    <div class="unlock-card">
        <h2>🎓 Desbloqueie o Acesso Completo</h2>
        <p>Faça login para ter acesso total à biblioteca digital da UnB, incluindo downloads ilimitados e funcionalidades exclusivas.</p>
        <a href="/login" class="btn">🚀 Fazer Login Agora</a>
    </div>
</section>
