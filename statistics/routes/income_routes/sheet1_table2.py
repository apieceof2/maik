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
        self.aggregation_key = ''
        self.is_aggregate = False

    def _get_tri_data(self, q=None, start_row=0):
        """
        从q中的数据整理出数据
        :param q: 所有要统计的数据
        :return:
        """
        people = 0
        revenue = 0
        yin_num = 0
        yin_value = 0
        card_num = 0
        card_value = 0
        from models.income import Income
        temp = self.data['vars']['duration'].split('-')
        duration = [temp[0], temp[1]]
        q = Income.find_during(duration)
        for i in q:
            people += i.value_by_key('people_num_by_cash')
            revenue += i.value_by_key('revenue')
            yin_num += i.people_sum_by_payment_type('银联+天交通二维码')
            card_num += i.people_sum_by_payment_type('实体卡（IC卡）')
            yin_value += i.value_sum_by_payment_type('银联+天交通二维码')
            card_value += i.value_sum_by_payment_type('实体卡（IC卡）')

        res = [
            [0, 2, revenue],
            [0, 3, people],
            [1, 2, yin_value],
            [1, 3, yin_num],
            [2, 2, card_value],
            [2, 3, card_num],
        ]
        return res

