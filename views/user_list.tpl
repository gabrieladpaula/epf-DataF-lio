% rebase('layout.tpl', title='Lista de Usuários', current_user=current_user)

<div class="container">
    <h1 class="mt-4">Gerenciamento de Usuários</h1>
    <p class="lead">Lista de todos os usuários cadastrados no sistema.</p>

    <table class="table table-striped table-hover mt-4">
        <thead class="thead-dark">
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Email</th>
                <th>Permissão</th>
                <th>Data de Nascimento</th>
            </tr>
        </thead>
        <tbody>
            % for user in users:
            <tr>
                <td>{{user['id']}}</td>
                <td>{{user['nome']}}</td>
                <td>{{user['email']}}</td>
                <td>
                    % if user['role'] == 'admin':
                        <span class="badge bg-primary">Administrador</span>
                    % else:
                        <span class="badge bg-secondary">Usuário</span>
                    % end
                </td>
                <td>{{user['birthdate'] or 'Não informada'}}</td>
            </tr>
            % end
        </tbody>
    </table>
</div>