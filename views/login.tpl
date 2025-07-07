%rebase('layout.tpl', title= 'Login')

<div class="pagina-login">
    <div class="login-box">
        <h2>Entrar na sua conta</h2>

        %if defined('error'):
            <div class="login-error">{{error}}</div>
        %end        

        <form action="/login" method="post">
            <label for="email">Endereço de E-mail</label>
            <input type="email" id="email" name="email" required>

            <label for="senha">Senha</label>
            <input type="password" id="senha" name="senha" required>

            <button type="submit">Entrar</button>
        </form>

        <p class="login-footer">
            Ainda não tem conta? <a href="/users/add">Registe-se aqui</a>.
        </p>
    </div>
</div>
