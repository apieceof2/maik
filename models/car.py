from .mongo import Mongo


class Car(Mongo):
    __fields__ = Mongo.__fields__ + [
        ('car_name', str, ''),
    ]

