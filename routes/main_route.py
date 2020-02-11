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

main = Blueprint('main', __name__)


@main.route('/<int:page>')
def index(page=1):
    posts, is_next = pagination(page)
    return render_template('index.html', posts = posts, is_next=is_next, page=page)


@main.route('/')
def index_no_args():
    posts, is_next = pagination(1)
    return render_template('index.html', posts = posts, is_next=is_next, page=1)


@main.route('/post_detail/<int:id>')
def post_detail(id):
    post = Post.find(id)
    return render_template('post_detail.html', post=post)


def pagination(page):
    start = page # 页码
    offset = Config['NUMBER_OF_PAGINATION'] # 每页的文章数
    start = (page - 1) * offset # 得到的是当前页的文章索引
    if (start + offset > Post.count()): # 判断是否还有下一页
        return Post.sub_find(start, offset), False 
    else:
        return Post.sub_find(start, offset), True

    

