from .mongo import Mongo


class Cashier(Mongo):
    __fields__ = Mongo.__fields__ + [
        ('cashier_name', str, ''),
    ]

