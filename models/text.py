from .mongo import Mongua

class Text(Mongua):
    __fields__ = Mongua.__fields__ + [
        ('id', int, -1),
        ('title', str, ''),
        ('content', str, ''),
    ]