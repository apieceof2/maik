from .decorator import update_route
from models.income import Income
from .utils import *
from .route import Route



@update_route('IncomeSta_test_sheet1')
class IncomeSheet1(Route):
    def __init__(self):
        self.data = {
            'vars': {
                'duration': '2012'
            },
            'data': []
        }
        self.DB = Income
        self.aggregation_key = 'route'





