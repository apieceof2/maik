from models.income import Income
from statistics.routes.router import Router


class IncomeSheet6Table1(Router):
    def __init__(self):
        super().__init__()
        self.DB = Income
        self.aggregation_key = 'route'

    def _aggregation_func(self, q):
        res = [
            getattr(q[0], 'route'),
            len(q)
        ]
        card_types = ['支付宝@']
        for card in card_types:
            num = 0
            value = 0.0
            for item in q:
                a = getattr(item, card)[0]
                if not a:
                    a = 0
                b = getattr(item, card)[1]
                if not b:
                    b = 0.0
                num += a
                value += b
            res.append(num)
            res.append(value)
        return res