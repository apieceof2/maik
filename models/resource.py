from models.mongo import Mongo


class Resource(Mongo):
    __fields__ = Mongo.__fields__ + [
        ('name', str, ''),
        ('resource_type', str, ''),
    ]