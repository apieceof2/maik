from .mongo import Mongo


class Income(Mongo):
    __fields__ = Mongo.__fields__ + [
        # 仅仅包括基本信息, Payment字段通过mongo.update() 加入
        ('date', str, ''),
        ('car', str, ''),
        ('route', str, ''),
        ('revenue', float, 0),
        ('cashier', str, ''),
        ('remnant_num', int, 0),
        ('remnant_value', float, 0),
        ('fake_num', int, 0),
        ('fake_value', float, 0),
        ('people_num_by_cash', int, 0),
        ('people_num_by_cal', int, 0),
        ('people_num_by_car', int, 0),
    ]




