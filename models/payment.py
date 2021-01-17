from .mongo import Mongo


class Payment(Mongo):
    __fields__ = Mongo.__fields__ + [
        ('name', str, ''),
        ('payment_type', str, ''),
    ]

    def __repr__(self):
        return '[ ' + getattr(self, 'payment_name', '') + ' , ' + getattr(self, 'payment_type_name', '') + ' ]'
