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

    @staticmethod
    def _aggregation_func(q):
        """

        :param q:
        :type q: models.Income
        :return:
        """
        res = [
            q[0].route,
            len(q),
        ]

        people_num_by_cash = 0
        revenue = 0.0
        for r in q:
            people_num_by_cash += r.people_num_by_cash
            revenue += r.revenue
        res.append(people_num_by_cash)
        res.append(revenue)
        return res






