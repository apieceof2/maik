from models.expend import Expend
from statistics.routes.router import Router


class ExpendSheet11Table1(Router):
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
        res = [
            getattr(q[0], 'car'),
        ]
        times = 0
        amount = 0.0
        price = 0.0
        for i in q:
            times += i.get_resource('准格尔旗交通投资有限公司', 0)
            amount += i.get_resource('准格尔旗交通投资有限公司', 1)
            price += i.get_resource('准格尔旗交通投资有限公司', 2)
        res.append(times)
        res.append(amount)
        res.append(price)

        return res






