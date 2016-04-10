# -*- coding: utf-8 -*-

from flask import Flask, request
from flask import render_template
from config import session
from models.user import User

app = Flask(__name__)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        session.add(user)
        return render_template('success.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = session.query(User).filter_by(username=username).first()
        if result.password == password:
            print u'登录成功'
        else :
            print u'登录失败'

if __name__ == '__main__':
    app.debug = True
    app.run()
