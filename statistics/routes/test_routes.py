from models.income import Income
from models.payment import Payment


def add(q, key):
    res = 0
    for i in q:
        res += getattr(i, key, 0)
    return res

def add_by_payment_type(q, payment_type):
    num = 0
    value = 0.0
    payments = Payment.find_by(payment_type=payment_type)
    for payment in payments:
        if payment.name == payment_type+'合计':
            continue
        for item in q:
            a = getattr(item, payment.name)[0]
            b = getattr(item, payment.name)[1]
            if a:
                num += a
            if b:
                value += b
    return num, value






def test():
    def foo(q):
        k = None
        v = None
        for k, v in q.items():
            pass
        r = []
        r.append(k)
        r.append(len(v))
        r.append( add(v, 'people_num_by_cash'))
        r.append(add(v, 'revenue'))

        c, d = add_by_payment_type(v, '实体卡（IC卡）')
        r.append(c)
        r.append(d)

        c, d = add_by_payment_type(v, '银联+天交通二维码')
        r.append(c)
        r.append(d)

        c = r[2] + r[4] + r[6]
        d = r[3] + r[5] + r[7]

        r.append(c)
        r.append(d)

        print(r)
    a = Income.aggregate(foo, 'route')


if __name__ == '__main__':
    test()
