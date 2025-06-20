from bottle import route, run, template, request, redirect, static_file

users = []

@route('/users')
def list_users():
    return template('users', users=users)

@route('/users/add')
def add_user_form():
    return template('user_form', action='/users/add', user=None)

@route('/users/add', method='POST')
def add_user():
    name = request.forms.get('name')
    email = request.forms.get('email')
    birthdate = request.forms.get('birthdate')
    user = {
        'id': len(users) + 1,
        'name': name,
        'email': email,
        'birthdate': birthdate
    }
    users.append(user)
    redirect('/users')

# ✅ Rota para carregar arquivos estáticos (CSS, JS, imagens)
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

# 🚀 Roda o servidor
if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True, reloader=True)
