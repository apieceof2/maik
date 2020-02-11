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

