from flask import (
    Blueprint,
    redirect,
    request,
    url_for,
    render_template,
    session,
    abort,
)

from config import Config

from models.post import Post

main = Blueprint('login', __name__)

@main.route('/login', methods=["GET"])
def login():
    if session.get('logged') == True:
        return redirect(url_for('main.index', page=1))
    return render_template('login.html')

@main.route('/logout')
def logout():
    session['logged'] = False 
    return redirect(url_for('main.index', page=1))

@main.route('/log', methods=['POST'])
def log():
    if request.form.get('password') == Config['PASSWORD']:
        session['logged'] = True
        return redirect(url_for('main.index', page=1))
    else:
        return "<h1>滚</h1>"


