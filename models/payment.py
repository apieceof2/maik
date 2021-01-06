from .mongo import Mongo
from bson import ObjectId


class Payment(Mongo):
    __fields__ = Mongo.__fields__ + [
        ('payment_name', str, ''),
        ('payment_type_name', str, ''),
    ]

    def __repr__(self):
        return '[ ' + getattr(self, 'payment_name', '') + ' , ' + getattr(self, 'payment_type_name', '') + ' ]'
