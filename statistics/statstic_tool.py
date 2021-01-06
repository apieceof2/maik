from models.record import Record
from models.payment import Payment


def _sum(query, key):
    # 获得一个query, 把其中的对象的key成员加起来返回
    sum = 0
    for i in query:
        m = getattr(i, key, 0)
        if m:
            sum += m
    return sum


def _count(q):
    # 用于聚合
    # 返回数量
    return len(q)


def _row(q):
    # 用于聚合
    # 不做任何处理, 直接返回list
    res = []
    for i in q:
        res.append(i.payment_name)
    return res

def date_max(q):
    max = '2000.00.00'
    for i in q:
        if max < getattr(i,'date', '0000.00.00'):
            max = getattr(i, 'date')
    return max


def _payment_sum(query, key):
    # 获得一个query, 把其中对象num, value 分别加起来, 组成(num, value)返回
    num_sum = 0
    value_sum = 0
    for i in query:
        item = getattr(i, key, 0)
        if item[0]:
            num_sum += item[0]
        if item[1]:
            value_sum += item[1]
    return num_sum, value_sum


def revenue_sum(query):
    return _sum(query, 'revenue')


def remnant_num_sum(query):
    return _sum(query, 'remnant_num')


def remnant_value_sum(query):
    return _sum(query, 'remnant_value')


def fake_num_sum(query):
    return _sum(query, 'fake_num')


def fake_value_sum(query):
    return _sum(query, 'fake_value')


def student_sum(query):
    return _payment_sum(query, '学生卡')


def old_sum(query):
    return _payment_sum(query, '敬老卡')


def common_sum(query):
    return _payment_sum(query, '普通卡')


def teacher_sum(query):
    return _payment_sum(query,'教师卡')


def better_sum(q):
    return _payment_sum(q, '优抚卡')


def offsite_sum(q):
    return _payment_sum(q, '异地卡')


def official_sum(q):
    return _payment_sum(q, '公务卡')


def silver_qrcode_sum(q):
    return _payment_sum(q, "银联二维码")


def silver_double_sum(q):
    return _payment_sum(q, '银联双免')


def silver_oda_sum(q):
    return _payment_sum(q, '银联ODA')


def sky_qrcode_sum(q):
    return _payment_sum(q, '天骄通二维码')


def aggregate_payment_type_name_by(func, key):
    # 对一个record中的支付方式相加, 记录到数据库
    # (key: payment_type_name+'num合计' , value=值)和(key:payment_type_name+'value合计', value=值)
    record_list = Record.find_all()
    payments = Payment.aggregate(_row, 'payment_type_name')
    for k, v in payments.items():
        num = k + "_num_" + "_sum"
        value = k + "_value_" + '_sum'
        form = {}
        for r in Record.find_all():
            form[num] = 0
            form[value] = 0
            for i in v:
                a_num = getattr(r, i, (0, 0))[0]
                if a_num:
                    form[num] += a_num
                a_num = getattr(r, i, (0, 0))[1]
                if a_num:
                    form[value] += a_num
                r.update(form, hard=True)






if __name__ == '__main__':
    aggregate_payment_type_name_by(_row, 'i')