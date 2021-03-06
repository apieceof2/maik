from models.expend import Expend
from statistics.routes.router import Router


class ExpendSheet8Table1(Router):

    def __init__(self):
        super().__init__()
        self.data = {
            'vars': {
                'duration': '',
            },
            'data': []
        }
        self.DB = Expend
        self.aggregation_key = 'car'
        self.is_aggregate = True

    def _aggregation_func(self, q):
        res = [getattr(q[0], 'car')]

        gus = 0.0
        cash = 0.0
        for i in q:
            gus += i.get_resource('准发加气城（4公里）', 1)
            cash += i.get_resource('准发加气城（4公里）', 3)
        res.append(gus)
        res.append(cash)
        return res







