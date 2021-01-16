from models.expend import Expend
from utils import *
from Config import EXPEND_CONFIG as Config


class Expend2Form():
    def __init__(self):
        for key, value in Config.items():
            setattr(self, str.lower(key), value)