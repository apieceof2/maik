from models.income import Income
from statistics.routes.router import Router


class IncomeSheet5Table1(Router):
    def __init__(self):
        super().__init__()
        self.DB = Income
        self.aggregation_key = 'route'

    def _aggregation_func(self, q):
        res = [
            getattr(q[0], 'route'),
            len(q)
        ]
        card_types = ['微信@']
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

    def test(self):
        a = Income.aggregate(self._aggregation_func, 'route')
        print(a)

if __name__ == '__main__':
    a = IncomeSheet5Table1('sheet5_table1')
    a.test()
