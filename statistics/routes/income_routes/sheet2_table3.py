from models.income import Income
from statistics.routes.router import Router


class IncomeSheet2Table3(Router):
    def __init__(self, table_name):
        super().__init__(table_name)
        self.DB = Income
        self.aggregation_key = 'cashier'

    def _aggregation_func(self, q):
        res = [getattr(q[0], 'cashier')]
        routes_msg = {}
        for item in q:
            route = getattr(item, 'route')
            num = getattr(item, 'fake_num')
            value = getattr(item, 'fake_value')
            if not num:
                num = 0
            if not value:
                value = 0
            if route in routes_msg:
                routes_msg[route][0] += num
                routes_msg[route][1] += value
            else:
                routes_msg[route] = [num, value]

        routes_list = ['1路', '2路', '3路', '4路', '5路', '6路', '7路', '8路', '9路',
                       'K3路', 'K9路', 'K10路', '布尔陶亥', '苗家滩']
        for route in routes_list:
            if route in routes_msg:
                res.append(routes_msg[route][0])
                res.append(routes_msg[route][1])
            else:
                res.append(0)
                res.append(0.0)

        return res

    def test(self):
        a = Income.aggregate(self._aggregation_func, 'cashier')


if __name__ == '__main__':
    a = IncomeSheet2Table3('sheet2_table2')
    a.test()
