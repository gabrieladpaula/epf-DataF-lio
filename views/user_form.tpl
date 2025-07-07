% rebase('layout.tpl', title='Adicionar Usuário', current_user=current_user)

<style>
  .pagina-cadastro {
    background-color: #f8f8fa;
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem;
    box-sizing: border-box;
    margin: 0;
  }

  .cadastro-box {
    background: #fff;
    border: 4px solid #f97316;
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.05);
    max-width: 500px;
    width: 100%;
  }

  h1 {
    text-align: center;
    color: #333;
    margin-bottom: 1.5rem;
  }

  .form-group {
    margin-bottom: 1.2rem;
  }

  label {
    display: block;
    margin-bottom: 0.4rem;
    font-weight: 600;
    color: #444;
  }

  .form-control {
    width: 100%;
    padding: 0.7rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 0.95rem;
  }

  .user-actions {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 2rem;
  }

  .btn {
    padding: 0.7rem 2.2rem;
    border-radius: 10px;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    cursor: pointer;
    transition: background 0.2s;
  }

  .salvar-btn {
    background-color: #5e2ca5;
    color: #fff;
  }

  .salvar-btn:hover {
    background-color: #4b2290;
  }

  .voltar-btn {
    background-color: #d1d1d1;
    color: #333;
    text-decoration: none;
  }

  .voltar-btn:hover {
    background-color: #bbb;
  }
</style>

<div class="pagina-cadastro">
  <div class="cadastro-box">
    <h1>Adicionar Usuário</h1>
    <form action="/users/add" method="post">
      <div class="form-group">
        <label for="name">Nome:</label>
        <input type="text" id="name" name="name" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="birthdate">Data de Nascimento:</label>
        <input type="date" id="birthdate" name="birthdate" class="form-control">
      </div>
      <div class="form-group">
        <label for="senha">Senha:</label>
        <input type="password" id="senha" name="senha" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="confirmar_senha">Confirmar Senha:</label>
        <input type="password" id="confirmar_senha" name="confirmar_senha" class="form-control" required>
      </div>
      <div class="user-actions">
        <button type="submit" class="btn salvar-btn">Salvar</button>
        <a href="/" class="btn voltar-btn">Voltar</a>
      </div>
    </form>
  </div>
</div>
