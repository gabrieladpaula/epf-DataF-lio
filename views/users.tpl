%rebase('layout', title='Dashboard')

<section class="dashboard">

    <!-- 🧠 Top Cards -->
    <div class="cards">
        <div class="card pink">
            <h4>Total de Usuários</h4>
            <p class="number">1247</p>
            <span>+156 este mês</span>
        </div>
        <div class="card blue">
            <h4>Total de Livros</h4>
            <p class="number">89</p>
            <span>Biblioteca completa</span>
        </div>
        <div class="card green">
            <h4>Downloads</h4>
            <p class="number">3456</p>
            <span>+892 este mês</span>
        </div>
        <div class="card orange">
            <h4>Visualizações</h4>
            <p class="number">12890</p>
            <span>Total geral</span>
        </div>
    </div>

    <!-- 🔘 Botões de ação -->
    <div class="actions">
        <button class="btn purple">+ Gerenciar Obras</button>
        <button class="btn purple">+ Adicionar Livro</button>
        <button class="btn">Relatórios</button>
        <button class="btn">Configurações</button>
    </div>

    <!-- 🔍 Abas -->
    <div class="tabs">
        <a href="#" class="active">Visão Geral</a>
        <a href="#">Usuários</a>
        <a href="#">Livros Populares</a>
        <a href="#">Atividade Recente</a>
    </div>

    <!-- 📈 Crescimento -->
    <div class="panels">
        <div class="panel growth">
            <h3>📈 Crescimento Mensal</h3>
            <div class="data">
                <p>Novos Usuários <span class="positive">+156</span></p>
                <p>Downloads <span class="positive">+892</span></p>
                <div class="progress">
                    <div class="bar"></div>
                </div>
            </div>
        </div>

        <div class="panel status">
            <h3>⚙️ Status do Sistema</h3>
            <ul>
                <li>Servidor <span class="status online">Online</span></li>
                <li>Database <span class="status connected">Conectado</span></li>
                <li>Backup <span class="status updated">Atualizado</span></li>
            </ul>
        </div>
    </div>

</section>
