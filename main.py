# Importa as ferramentas do Bottle e o novo user_service
from bottle import route, run, template, request, redirect, static_file
from services import user_service

users = []  # Lista temporária para armazenar utilizadores

# Rota temporária para listar utilizadores
@route('/users')
def list_users():

    return template('users', users=users)

@route('/users/add')
def add_user_form():

    return template('user_form', action='/users/add', user=None)

@route('/users/add' , method='POST')
def add_user():
    # Recebe os dados do formulário e chama user_service para guardar no banco de SQLite.
    # Obter os dados do formulário
    nome = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')
    # Senha temporária.
    password = "senha123"
    sucesso = user_service.create_user(nome, email, password, birthdate)
    if sucesso:
        return redirect('/users')
    else:
        return "Ocorreu um erro ao criar o cadastro. O e-mail fornecido já pode estar em uso"
    
#Rota para carregar arquivos estáticos
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static') 

#Rota para o servidor
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True) 
