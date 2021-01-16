from .mongo import Mongo


class PaymentType(Mongo):
    __fields__ = Mongo.__fields__ + [
        ('name', str, ''),
    ]