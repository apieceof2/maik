from models.expend import Expend
from statistics.routes.router import Router


class ExpendSheet13Table1(Router):
    def __init__(self):
        super().__init__()
        self.data = {
            'vars': {
                'duration': ''
            },
            'data': []
        }
        self.DB = Expend
        self.aggregation_key = 'route'
        self.is_aggregate = True

    def _aggregation_func(self, q):
        res = [
            getattr(q[0], 'route'),
            len(q)
        ]
        p_sum = 0
        p_price = 0
        g_sum = 0
        g_price = 0
        e_sum = 0
        e_price= 0
        for i in q:
            p_sum += i.get_resource_amount_sum('加油站')
            p_price += i.get_resource_price_sum('加油站')
            g_sum += i.get_resource_amount_sum('加气站')
            g_price += i.get_resource_price_sum('加气站')
            e_sum += i.get_resource_amount_sum('充电站')
            e_price += i.get_resource_price_sum('充电站')

        res.append(p_sum)
        res.append(g_sum)
        res.append(e_sum)
        res.append(p_price)
        res.append(g_price)
        res.append(e_price)
        return res






