from .mongo import Mongo


class Route(Mongo):
    __fields__ = Mongo.__fields__ + [
        ('route_name', str, ''),
    ]

