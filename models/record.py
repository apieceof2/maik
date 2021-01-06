from .mongo import Mongo
from .car import Car
from .cashier import Cashier
from bson import ObjectId
from .route import Route
from .payment import Payment


class Record(Mongo):
    __fields__ = Mongo.__fields__ + [
        ('date', str, ''),
        ('car_name', str, ''),
        ('route_name', str, ''),
        ('revenue', float, 0),
        ('cashier_name', str, ''),
        ('remnant_num', int, 0),
        ('remnant_value', float, 0),
        ('fake_num', int, 0),
        ('fake_value', float, 0),
    ]




