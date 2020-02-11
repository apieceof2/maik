import os.path
import time
import json
from flask import session, abort, url_for, redirect
from functools import wraps


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    with open('gua.log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def validate_login(f):
    # 验证登录的装饰器
    @wraps(f)
    def decorate(*args, **kwargs):
        if session.get('logged', False):
            return f(*args, **kwargs)
        else:
            abort(404)
    return decorate



# 检测是否登录的decorator
def login_required(func):
    def wrapper(*args, **kwargs):
        if session.get('logged') == True:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login.login'))
    return wrapper

