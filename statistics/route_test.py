from functools import wraps
config = {}

def get_data(log='route'):
    def decorator(func):
        config[log] = log
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(log)
            print('start')
            print(func(*args, **kwargs))
            print('end')
        return wrapper
    return decorator

@get_data("route")
def sheet1():
    return "this is income sheet1"

@get_data('wa')
def sheet2():
    pass

if __name__ == '__main__':
    print(config)