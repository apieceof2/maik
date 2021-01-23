from models.income import Income
from statistics.routes.router import Router


class IncomeSheet3Table1(Router):
    def __init__(self, table_name):
        super().__init__(table_name)
        self.DB = Income
        self.aggregation_key = 'route'

    def _aggregation_func(self, q):
        res = [
            getattr(q[0], 'route'),
            len(q)
        ]
        card_types = ['学生卡', '敬老卡', '普通卡', '教师卡', '优抚卡', '异地卡', '公务卡']
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
    a = IncomeSheet3Table1('sheet3_table1')
    a.test()
