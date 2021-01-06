from .mongo import Mongo


class PaymentType(Mongo):
    __fields__ = Mongo.__fields__ + [
        ('payment_type_name', str, ''),
    ]