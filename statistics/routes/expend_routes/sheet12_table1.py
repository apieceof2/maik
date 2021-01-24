from models.expend import Expend
from statistics.routes.router import Router


class ExpendSheet12Table1(Router):
    def __init__(self, car):
        self.car = car
        super().__init__()
        self.data = {
            'vars': {
                'duration': '',
                'car': self.car
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
            res.append([row, 2, expend.get_resource('准格尔旗交通投资有限公司', 0)])
            res.append([row, 3, expend.get_resource('准格尔旗交通投资有限公司', 1)])
            res.append([row, 4, expend.get_resource('准格尔旗交通投资有限公司', 2)])

            row += 1
        return res



