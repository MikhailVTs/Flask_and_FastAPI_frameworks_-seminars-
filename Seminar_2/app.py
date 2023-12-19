from flask import Flask, render_template, request, redirect, make_response
from flask import url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        name = request.form['username']

        email = request.form['email']
         # Создание cookie-файла с данными пользователя
        response = make_response(redirect('/welcome'))
        response.set_cookie('username', name)

        response.set_cookie('email', email)
        return response
    
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    # Получение данных пользователя из cookie-файла
    name = request.cookies.get('username')
    
    if name:

        return render_template('welcome.html', name=name)
    else:

        return redirect('/')


@app.route('/logout')
def logout():
    # Удаление cookie-файла с данными пользователя
    response = make_response(redirect('/'))
    response.delete_cookie('username')
    response.delete_cookie('email')
    
    return response

if __name__ == '__main__':
    app.run(debug=True)