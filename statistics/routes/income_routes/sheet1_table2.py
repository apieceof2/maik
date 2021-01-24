from models.income import Income
from statistics.routes.router import Router
from models.payment import Payment


class IncomeSheet1Table2(Router):
    def __init__(self):
        super().__init__()
        self.data = {
            'vars': {
                'duration': '2012'
            },
            'data': [
            ]
        }
        self.DB = Income
        self.aggregation_key = 'route'
        self.is_aggregate = False

    @staticmethod
    def _sum_by_payment_type(q, payment_type_name):
        """
        统计某一个记录集合中某一个payment_type的人次, 金额
        :param q: model的list
        :param payment_type_name: payment_type的name
        :return: (num, value)
        """
        num = 0
        value = 0.0
        payments = Payment.find_by(payment_type=payment_type_name)
        for payment in payments:
            if payment.name == payment.payment_type+'合计':
                continue
            for i in q:
                temp = getattr(i, payment.name)
                if temp[0]:
                    num += temp[0]
                if temp[1]:
                    value += temp[1]
        res = (num, value)
        return res

    def _get_tri_data(self, q, start_row):
        """
        从q中的数据整理出数据
        :param q: 所有要统计的数据
        :return:
        """
        a = self.sum_by_key(q, 'revenue', float)
        b = self.sum_by_key(q, 'people_num_by_cash', int)
        c = self._sum_by_payment_type(q, '实体卡（IC卡）')
        d = self._sum_by_payment_type(q, '银联+天交通二维码')
        data = [
            (0 + start_row, 2, a),
            (0 + start_row, 3, b),
            (1 + start_row, 2, c[1]),
            (1 + start_row, 3, c[0]),
            (2 + start_row, 2, d[1]),
            (2 + start_row, 3, d[0]),
            (3 + start_row, 2, a + c[1] + d[1]),
            (3 + start_row, 3, b + c[0] + d[0]),
        ]
        return data