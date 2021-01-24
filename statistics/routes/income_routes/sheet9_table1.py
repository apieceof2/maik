from models.income import Income
from statistics.routes.router import Router


class IncomeSheet9Table1(Router):
    def __init__(self):
        super().__init__()
        self.DB = Income
        self.aggregation_key = 'car'

    def _aggregation_func(self, q):
        res = [
            getattr(q[0], 'car'),
        ]

        # calculate the number of days of this car
        number_of_days = {}
        for i in q:
            date = getattr(i, 'date')
            if date in number_of_days:
                number_of_days[i] += 1
            else:
                number_of_days[i] = 1
        res.append(len(number_of_days))

        # the sum of revenue
        revenue_sum = 0
        for i in q:
            revenue_sum += i.value_by_key('revenue')
        res.append(revenue_sum)

        a = 0
        b = 0
        c = 0
        d = 0
        for i in q:
            a += i.value_sum_by_payment_type('实体卡（IC卡）')
            b += i.value_sum_by_payment_type('银联+天交通二维码')
            c += i.value_sum_by_payment_type('微信')
            d += i.value_sum_by_payment_type('支付宝')
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
                temp += i.payment_value_by_key(payment)
            res.append(temp)

        return res
