<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard - DataFólio</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Inter', sans-serif;
    }

    body {
      background-color: #f8f8fa;
      padding: 2rem;
    }

    .dashboard {
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1.5rem;
    }

    .card {
      background-color: #fff;
      padding: 1.5rem;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }

    .card h3 {
      font-size: 1rem;
      color: #5e2ca5;
      margin-bottom: 0.5rem;
    }

    .card p {
      font-size: 1.5rem;
      font-weight: bold;
      color: #000;
    }

    .info {
      font-size: 0.9rem;
      color: #555;
    }

    .dashboard-buttons {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .btn {
      background-color: #5e2ca5;
      color: #fff;
      padding: 0.7rem 1.2rem;
      border: none;
      border-radius: 8px;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s;
    }

    .btn:hover {
      background-color: #4b2290;
    }

    .extras {
      background-color: #fff;
      padding: 1.5rem;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }

    .extras h3 {
      color: #5e2ca5;
      margin-bottom: 0.5rem;
      font-size: 1.2rem;
    }

    .extras ul {
      margin-top: 0.5rem;
      padding-left: 1rem;
    }

    .extras li {
      margin-bottom: 0.3rem;
    }
  </style>
</head>
<body>
  <main class="dashboard">
    <section class="cards">
      <div class="card">
        <h3>Total de Usuários</h3>
        <p>1247</p>
        <span class="info">+156 este mês</span>
      </div>
      <div class="card">
        <h3>Total de Livros</h3>
        <p>89</p>
        <span class="info">Biblioteca completa</span>
      </div>
      <div class="card">
        <h3>Downloads</h3>
        <p>3456</p>
        <span class="info">+892 este mês</span>
      </div>
      <div class="card">
        <h3>Visualizações</h3>
        <p>12890</p>
        <span class="info">Total geral</span>
      </div>
    </section>

    <div class="dashboard-buttons">
      <button class="btn">+ Gerenciar Obras</button>
      <button class="btn">+ Adicionar Livro</button>
      <button class="btn">Relatórios</button>
      <button class="btn">Configurações</button>
    </div>

    <section class="extras">
      <h3>📈 Crescimento Mensal</h3>
      <p>Novos Usuários +156</p>
      <p>Downloads +892</p>

      <h3>⚙️ Status do Sistema</h3>
      <ul>
        <li>Servidor Online</li>
        <li>Database Conectado</li>
        <li>Backup Atualizado</li>
      </ul>
    </section>
  </main>
</body>
</html>
