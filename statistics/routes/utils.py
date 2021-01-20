from models.payment import Payment

def make_tri(li):
    """
    将一个li变成一个三元组的list
    :param li: 一个字典
    :return:
    """


def add(q, key):
    """
    将某个关键子相同的项目的值加到到一起
    :param q:
    :param key:
    :return:
    """
    res = 0
    for i in q:
        res += getattr(i, key, 0)
    return res


def add_by_payment_type(q, payment_type):
    """
    Payment 合计
    :param q:
    :param payment_type:
    :return:
    """
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


