from models.expend import Expend
from statistics.routes.router import Router


class ExpendSheet4Table1(Router):
    """
    中石油加油汇总
    """
    def __init__(self, car):
        super().__init__()
        self.car = car
        self.data = {
            'vars': {
                'duration': '',
                'car': self.car,
            },
            'data': []
        }
        self.DB = Expend
        self.aggregation_key = ''
        self.is_aggregate = True

    def _aggregation_func(self, q):
        return []

    def _get_tri_data(self, start_row=0):
        from models.expend import Expend
        expends = Expend.find_by(car=self.car)
        row = 0
        res = []
        for expend in expends:
            res.append([row, 0, expend.get_by_key('date')])
            res.append([row, 1, expend.get_by_key('route')])
            for i in range(0, 5):
                res.append([row, i + 2, expend.get_resource('亿通（加油站）1', i)])
            for i in range(0, 5):
                res.append([row, i + 8, expend.get_resource('亿通（加油站）2', i)])
            row += 1
        return res





