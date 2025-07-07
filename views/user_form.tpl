%rebase('layout.tpl', title='Adicionar Usuário', current_user=current_user, pagina_class='pagina-cadastro')

<div class="cadastro-box">
  <h2>Adicionar Usuário</h2>
  <form action="{{action}}" method="post">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" value="{{user.get('nome', '')}}" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" value="{{user.get('email', '')}}" required>

    <label for="nascimento">Data de Nascimento:</label>
    <input type="date" id="nascimento" name="nascimento" value="{{user.get('nascimento', '')}}" required>

    <label for="senha">Senha:</label>
    <input type="password" id="senha" name="senha" required>

    <label for="confirmar_senha">Confirmar Senha:</label>
    <input type="password" id="confirmar_senha" name="confirmar_senha" required>

    <div class="user-actions">
      <button type="submit" class="btn salvar-btn">Salvar</button>
      <a href="/users" class="btn voltar-btn">Voltar</a>
    </div>
  </form>
</div>
