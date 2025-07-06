from bottle import route, run, template, request, redirect, static_file, response, BaseRequest
from services import user_service, livro_service, genero_service
from services.auth_service import get_current_user, admin_required
from config import Config
import os

BaseRequest.MEMFILE_MAX = 10 * 1024 * 1024

@route('/')
def index():
    return redirect('/catalogo')

@route('/login', method='GET')
def get_login():
    user = get_current_user()
    return template('login', error=None, current_user=user)

@route('/login', method='POST')
def post_login():
    email = request.forms.get('email')
    senha = request.forms.get('senha')
    user = user_service.check_login(email, senha)
    if user:
        response.set_cookie("user_email", user['email'], secret=Config.SECRET_KEY)
        return redirect('/catalogo')
    else:
        user = get_current_user()
        return template('login', error='E-mail ou senha inválidos.', current_user=user)

@route('/logout')
def logout():
    response.delete_cookie("user_email", secret=Config.SECRET_KEY)
    return redirect('/login')

@route('/users/add', method='GET')
def add_user_form():
    user = get_current_user()
    return template('user_form', action='/users/add', user=None, current_user=user)

@route('/users/add', method='POST')
def add_user():
    nome = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')
    senha = request.forms.get('senha')
    confirmar_senha = request.forms.get('confirmar_senha')

    if senha != confirmar_senha:
        return "Erro: As senhas não coincidem. Por favor, tente novamente."

    sucesso = user_service.create_user(nome, email, senha, birthdate)
    
    if sucesso:
        return redirect('/login')
    else:
        return "Ocorreu um erro ao criar o utilizador. O e-mail fornecido já pode estar em uso."
    
@route('/admin')
@admin_required
def admin_dashboard():
    user = get_current_user()
    return template('admin_dashboard', current_user=user) 

@route('/users')
@admin_required
def list_users():
    user = get_current_user()
    return template('users', users=[], current_user=user)

@route('/books')
@admin_required
def list_books():
    user = get_current_user()
    livros_reais = livro_service.get_all_books()
    return template('books', books=livros_reais, current_user=user)

@route('/books/add', method='GET')
@admin_required
def add_book_form():
    user = get_current_user()
    todos_os_generos = genero_service.get_all_genres()
    return template('books_form', action='/books/add', current_user=user, generos=todos_os_generos)

@route('/books/add', method='POST')
@admin_required
def add_book():
    titulo = request.forms.get('title')
    autor = request.forms.get('author')
    sinopse = request.forms.get('sinopse')
   
    caminho_pdf_db = request.forms.get('caminho_pdf')
    generos_selecionados = request.forms.getall('generos')

    novo_livro_id = livro_service.create_book(titulo, autor, sinopse, caminho_pdf_db)

    if novo_livro_id:
        if generos_selecionados:
            livro_service.link_book_to_genres(novo_livro_id, generos_selecionados)
        return redirect('/books')
    else:
        return "Ocorreu um erro ao adicionar o livro."

@route('/books/edit/<livro_id:int>')
@admin_required
def edit_book_form(livro_id):
    book = livro_service.get_book_by_id(livro_id)
    if book:
        user = get_current_user()
        todos_os_generos = genero_service.get_all_genres()
        generos_do_livro_ids = livro_service.get_genres_por_book(livro_id)
        return template('edit_book_form', book=book, current_user=user, generos=todos_os_generos, generos_atuais=generos_do_livro_ids)
    else:
        return "Erro: Livro não encontrado."

@route('/books/edit/<livro_id:int>', method='POST')
@admin_required
def edit_book_action(livro_id):
    titulo = request.forms.get('title')
    autor = request.forms.get('author')
    sinopse = request.forms.get('sinopse')
    caminho_pdf = request.forms.get('caminho_pdf')
    generos_selecionados = request.forms.getall('generos')
    
    sucesso = livro_service.update_book(livro_id, titulo, autor, sinopse, caminho_pdf)
    if sucesso:
        livro_service.update_livro_generos(livro_id, generos_selecionados)
        return redirect('/books')
    else:
        return "Ocorreu um erro ao tentar atualizar o livro."

@route('/books/delete/<livro_id:int>', method='POST')
@admin_required
def delete_book_action(livro_id):
    sucesso = livro_service.delete_book(livro_id)
    if sucesso:
        return redirect('/books')
    else:
        return "Ocorreu um erro ao tentar apagar o livro."
    
@route('/catalogo')
def catalogo_livros():
    user = get_current_user()
    termo_busca = request.query.get('busca')

    if termo_busca:
        lista_de_livros = livro_service.search_books(termo_busca)
    else:
        lista_de_livros = livro_service.get_all_books()

    return template('catalogo',
                    current_user=user,
                    books=lista_de_livros,
                    termo_busca=termo_busca)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static') 

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)