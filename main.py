from bottle import route, run, template, request, redirect, static_file, response
from services import user_service, auth_service
from config import Config

users = [] 
books = []

@route('/users')
def list_users():
    user = auth_service.get_current_user()
    return template('users', users=users, current_user=user)

@route('/users/add')
def add_user_form():
    user = auth_service.get_current_user()
    return template('user_form', action='/users/add', user=None, current_user=user)

@route('/users/add', method='POST')
def add_user():
    nome = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')
    password = "senha123"
    
    sucesso = user_service.create_user(nome, email, password, birthdate)
    
    if sucesso:
        return redirect('/login')
    else:
        return "Ocorreu um erro ao criar o utilizador. O e-mail fornecido já pode estar em uso."

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

@route('/login', method='GET')
def get_login():
    user = auth_service.get_current_user()
    return template('login', error=None, current_user=user)

@route('/login', method='POST')
def post_login():
    email = request.forms.get('email')
    senha = request.forms.get('senha')
    user = user_service.check_login(email, senha)

    if user:
        response.set_cookie("user_email", user['email'], secret=Config.SECRET_KEY)
        return redirect('/users')
    else:
        user = auth_service.get_current_user()
        return template('login', error='E-mail ou senha inválidos.', current_user=user)

@route('/logout')
def logout():
    response.delete_cookie("user_email", secret=Config.SECRET_KEY)
    return redirect('/login')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static') 

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
