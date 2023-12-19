from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import sqlite3
import hashlib


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Получаем данные из формы
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        # Хешируем пароль
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Подключаемся к базе данных
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # Вставляем данные в таблицу пользователей
        c.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?,?,?,?)",
                  (first_name, last_name, email, hashed_password))

        # Сохраняем изменения в базе данных
        conn.commit()

        # Закрываем соединение с базой данных
        conn.close()

        return 'Пользователь успешно зарегистрирован!'
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

