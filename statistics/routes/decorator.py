from functools import wraps

routes = {}


def update_route(route_name):
    def wrapper(cls):
        obj = cls()
        routes[route_name] = obj
        return obj

    return wrapper
