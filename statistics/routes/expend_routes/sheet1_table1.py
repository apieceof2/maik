from models.expend import Expend
from statistics.routes.router import Router


class ExpendSheet1Table1(Router):
    """
    亿通加油站加油汇总
    """
    def __init__(self, gus_type='20#', price=0.0):
        super().__init__()
        self.gus_type = gus_type
        self.price = price
        self.data = {
            'vars': {
                'duration': '',
                'gus_type': self.gus_type,
                'price': self.price
            },
            'data': []
        }
        self.DB = Expend
        self.aggregation_key = 'car'
        self.is_aggregate = True

    def _aggregation_func(self, q):
        """
        亿通有点特别, 有亿通1, 亿通2两个字段, 需要整合起来
        :param q:
        :return:
        """
        if not q:
            return []
        res = [
            getattr(q[0], 'car')
        ]

        amount = 0.0
        price = 0.0
        price_after_off = 0.0
        for i in q:
            gus_type = i.get_resource('亿通（加油站）1', 0)
            gus_price = i.get_resource('亿通（加油站）1', 1)
            if gus_type == self.gus_type and str(gus_price) == str(self.price):
                amount += i.get_resource('亿通（加油站）1', 2)
                price += i.get_resource('亿通（加油站）1', 3)
                price_after_off += i.get_resource('亿通（加油站）1', 4)
        for i in q:
            gus_type = i.get_resource('亿通（加油站）2', 0)
            gus_price = i.get_resource('亿通（加油站）2', 1)
            if gus_type == self.gus_type and str(gus_price) == str(self.price):
                amount += i.get_resource('亿通（加油站）2', 2)
                price += i.get_resource('亿通（加油站）2', 3)
                price_after_off += i.get_resource('亿通（加油站）2', 4)
        res.append(amount)
        res.append(price)
        res.append(price_after_off)

        return res


