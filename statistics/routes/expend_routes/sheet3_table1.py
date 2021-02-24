from models.expend import Expend
from statistics.routes.router import Router


class ExpendSheet3Table1(Router):
    """
    中石油加油汇总
    """
    def __init__(self, gus_type='20#', price=0.0):
        super().__init__()
        self.gus_type = gus_type
        self.price = price
        self.data = {
            'vars': {
                'duration': '',
                'gus_type': self.gus_type,
                'price': self.price,
            },
            'data': []
        }
        self.DB = Expend
        self.aggregation_key = 'car'
        self.is_aggregate = True

    def _aggregation_func(self, q):
        """
        中石油
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
            gus_type = i.get_resource('中石油（加油站）', 0)
            if gus_type == self.gus_type:
                amount += i.get_resource('中石油（加油站）', 2)
                price += i.get_resource('中石油（加油站）', 3)
                price_after_off += i.get_resource('中石油（加油站）', 4)
        res.append(amount)
        res.append(price)
        res.append(price_after_off)

        return res


