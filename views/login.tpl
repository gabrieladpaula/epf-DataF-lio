%# Inclui o layout base
%rebase('layout.tpl', title='Login')

<div class="container">
    <h2>Acessar sua Conta</h2>

    % if error:
        <div style="color: red; border: 1px solid red; padding: 10px; margin-bottom: 15px;">
            {{error}}
        </div>
    % end        

    <form action="/login" method="post">
        <div class="mb-3">
            <label for="email" class="form-label">Endereço de E-mail</label>
            <input type="email" class="form-control" id="email" name="email" required>
        </div>

        <div class="mb-3">
            <label for="senha" class="form-label">Senha</label>
            <input type="password" class="form-control" id="senha" name="senha" required>
        </div>

        <button type="submit" class="btn btn-primary">Entrar</button>
    </form>

    <p style="margin-top: 15px;">Ainda não tem conta? <a href="/users/add">Registre-se aqui</a>.</p>
</div>
    
    
    
