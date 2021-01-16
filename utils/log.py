
def log(*args, message='log', end=''):
    print('[' + message, end='')
    for i in args:
        print(i, end=end)
    print(']')

