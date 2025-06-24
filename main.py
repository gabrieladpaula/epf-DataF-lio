from bottle import route, run, template, request, redirect, static_file, response
from services import user_service

users = []
books = []


# Rotas de usuários
@route('/users')
def list_users():
    return template('users', users=users)

@route('/users/add')
def add_user_form():
    return template('user_form', action='/users/add', user=None)

@route('/users/add', method='POST')
def add_user():
    nome = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')
    password = "senha123"
    sucesso = user_service.create_user(nome, email, password, birthdate)
    if sucesso:
        return redirect('/users')
    else:
        return "Erro ao criar usuário."

# Rotas de livros 📚
@route('/books')
def list_books():
    return template('books', books=books)

@route('/books/add')
def add_book_form():
    return template('books_form', action='/books/add')

@route('/books/add', method='POST')
def add_book():
    title = request.forms.get('title')
    author = request.forms.get('author')
    genre = request.forms.get('genre')
    book = {
        'id': len(books) + 1,
        'title': title,
        'author': author,
        'genre': genre
    }
    books.append(book)
    redirect('/books')


# Rota para arquivos estáticos
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

# Login e Logout
@route('/login')
def get_login():
    return template('login')

@route('/login', method='POST')
def post_login():
    email = request.forms.get('email')
    senha = request.forms.get('senha')
    user = user_service.check_login(email, senha)
    if user:
        response.set_cookie("user_email", user['email'], secret='uma-chave-secreta')
        return redirect('/users')
    else:
        return template('login', error='E-mail ou senha inválidos.')

@route('/logout')
def logout():
    response.delete_cookie("user_email")
    return redirect('/login')


# 🚀 Inicia o servidor
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
