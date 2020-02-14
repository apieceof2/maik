from .mongo import Mongua


class Post(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('user_id', int, -1),
        ('title', str, ''),
        ('content', str, ''),
        ('url', str, ''),
        ('html', str, ''),
        ('confidential',bool, False),
    ]

    @classmethod
    def sub_find(cls, start, offset):
        name = cls.__name__
        ds =cls.all_sorted_by_id()
        res = [i for i in ds]
        return res