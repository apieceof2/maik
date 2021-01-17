from .mongo import Mongo


class Expend(Mongo):
    __fields__ = Mongo.__fields__ + [
        # 仅仅包括基本信息, Payment字段通过mongo.update() 加入
        ('date', str, ''),
        ('car', str, ''),
        ('route', str, ''),

    ]

