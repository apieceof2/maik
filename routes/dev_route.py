from flask import (
    Blueprint,
    redirect,
    url_for,
    render_template,
    request,
    session,
)
from utils import login_required, validate_login
from models.post import Post 


main = Blueprint('dev', __name__)


@main.route('/add', methods=['POST'])
def add():
    form = request.form 
    Post.new(form)
    return redirect(url_for('dev.post'))


@main.route('/post', methods=['GET'])
@validate_login
def post():
    return render_template('post.html')


@main.route('/edit/<int:post_id>')
@validate_login
def edit(post_id):
    post = Post.find(post_id)
    return render_template('edit.html', post=post)

@main.route('/update/<int:post_id>', methods=['POST'])
@validate_login
def update(post_id):
    post = Post.find(post_id)
    post.update(request.form)
    return redirect(url_for('main.index', page=1))
