# -*- coding: utf-8 -*-

from flask import Flask, request, session
from flask import render_template
from config import db
from models.post import Post
from models.user import User
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username, password)
        db.add(user)
        db.commit()
        return render_template('info.html', message=u'注册成功', redirect='/login')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = db.query(User).filter_by(username=username).first()
        if result:
            if result.password == password:
                session['username'] = username
                return render_template('info.html', message=u'登录成功', redirect='/posts')
            else:
                return render_template('info.html', message=u'登录失败', redirect='/login')
        else:
            return render_template('info.html', message=u'用户不存在', redirect='/login')


@app.route('/logout/', methods=['GET'])
def logout():
    session.pop('username', None)
    return render_template('info.html', message=u'注销成功', redirect='/login')


@app.route('/publish/', methods=['GET', 'POST'])
def publish():
    if request.method == 'GET':
        if not session.has_key('username'):
            return render_template('info.html', message=u'尚未登录', redirect='/login')
        return render_template('publish.html')
    elif request.method == 'POST':
        title = request.form['title'].encode('utf-8', 'ignore')
        content = request.form['content'].encode('utf-8', 'ignore')
        username = session['username']
        post = Post(title, content, username)
        db.add(post)
        db.commit()
        return render_template('info.html', message=u'发布成功', redirect='/posts')


@app.route('/posts/', methods=['GET'])
def posts():
    if not session.has_key('username'):
        return render_template('info.html', message=u'尚未登录', redirect='/login')
    posts = db.query(Post).all()
    return render_template('posts.html', posts=posts)


@app.route('/post/<int:id>', methods=['GET'])
def post(id):
    if not session.has_key('username'):
        return render_template('info.html', message=u'尚未登录', redirect='/login')
    post = db.query(Post).filter_by(id=id).first()
    if post:
        return render_template('show.html', post=post)
    else:
        return render_template('info.html', message=u'公告不存在', redirect='/posts')


if __name__ == '__main__':
    app.debug = True
    app.run()
