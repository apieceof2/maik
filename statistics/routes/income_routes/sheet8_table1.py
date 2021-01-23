from models.income import Income
from statistics.routes.router import Router
from models.payment import Payment


class IncomeSheet8Table1(Router):
    def __init__(self, table_name):
        super().__init__(table_name)
        self.DB = Income
        self.aggregation_key = 'route'

    def _aggregation_func(self, q):
        res = [
            getattr(q[0], 'route'),
        ]

        # the sum of people_number_by_cal, car, cash
        cal = 0
        car = 0
        cash = 0
        for i in q:
            cal += i.value_by_key('people_num_by_cal')
            car += i.value_by_key('people_num_by_car')
            cash += i.value_by_key('people_num_by_cash')
        res.append(cal)
        res.append(car)
        res.append(cash)

        a = 0
        b = 0
        c = 0
        d = 0
        for i in q:
            a += i.people_sum_by_payment_type('实体卡（IC卡）')
            b += i.people_sum_by_payment_type('银联+天交通二维码')
            c += i.people_sum_by_payment_type('微信')
            d += i.people_sum_by_payment_type('支付宝')
        res.append(a)
        res.append(b)
        res.append(c)
        res.append(d)

        # other payments
        payments = ["学生卡",
                    "敬老卡",
                    "普通卡",
                    "教师卡",
                    "优抚卡",
                    "异地卡",
                    "公务卡",
                    "银联二维码",
                    "银联双免",
                    "银联ODA",
                    "天骄通二维码",
                    "微信@",
                    "支付宝@"]
        for payment in payments:
            temp = 0
            for i in q:
                temp += i.payment_num_by_key(payment)
            res.append(temp)

        return res
