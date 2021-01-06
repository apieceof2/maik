from .mongo import Mongo


class StaticByCarID(Mongo):
    __fields__ = Mongo.__fields__ + [
        ('car_id', str, ''),
        ('cash', float, ''),
        ('remnant_num', int, 0),
        ('remnant_value', float, 0),
        ('fake_num', int, 0),
        ('fake_value', float, 0)
    ]