from flask import Flask 
from flask_moment import Moment
from config import Config
from flask import session


app = Flask(__name__)
app.secret_key = 'test for good'
moment = Moment(app)

from routes.main_route import main as route_index
app.register_blueprint(route_index, url_prex='/')
from routes.dev_route import main as route_dev 
app.register_blueprint(route_dev, url_prex='/dev')
from routes.login_route import main as route_login 
app.register_blueprint(route_login, url_prex='/login')

def sub (md):
    post_sub_len = Config['POST_SUB_LEN']
    return md[:post_sub_len]
env = app.jinja_env
env.filters['sub'] = sub


if __name__ == '__main__':
    config = dict (
        debug = True,
        host = '0.0.0.0',
        port = 2000,
    )
    app.run(**config)



