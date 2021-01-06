import xlrd
from models.record import Record
from models.paymentType import PaymentType
from models.payment import Payment
from models.car import Car
from models.cashier import Cashier
from models.route import Route
from bson import ObjectId
from Config import FORMAT_CONFIG as CONFIG


def _open_excel(filename):
    sheet = xlrd.open_workbook(filename).sheet_by_index(0)
    return sheet


class Excel2Form(object):
    def __init__(self, filename):
        self.sheet = _open_excel(filename)
        self.payment_type_row = CONFIG['PAYMENT_TYPE_ROW']
        self.payment_start_col = CONFIG['PAYMENT_START_COL']
        self.payment_end_col = self.sheet.ncols
        self.record_start_row = CONFIG['RECORD_START_ROW']

        self.record_car_name_col = CONFIG['RECORD_CAR_ID_COL']
        self.record_route_name_col = CONFIG['RECORD_ROUTE_NAME_COL']
        self.record_revenue_col = CONFIG['RECORD_REVENUE_COL']
        self.record_cashier_name_col = CONFIG['RECORD_CASHIER_NAME_COL']
        self.record_remnant_col = CONFIG['RECORD_REMNANT_COL']
        self.record_fake_col = CONFIG['RECORD_FAKE_COL']

        self.title_row = CONFIG['TITLE_ROW']
        self.date_col = CONFIG['DATE_ROW']
        self.record_end_row = self._get_record_end_row()

    def _get_record_end_row(self):
        i = 0
        for i in range(self.record_start_row, self.sheet.nrows):
            if self.sheet.cell_value(i, self.record_car_name_col):
                continue
            else:
                break
        return i

    def get_cell_value(self, row, col, t):
        m = self.sheet.cell_value(row, col)
        if m:
            return t(m)

    def read_line(self, row):
        # 读取一行记录, 加入数据库, 日期和车名路线唯一确定一条记录, 如果重复则更新
        form = {}
        form['date'] = self.get_cell_value(self.date_col, 0, str)
        form['car_name'] = self.get_cell_value(row, self.record_car_name_col, str)
        form['route_name'] = self.get_cell_value(row, self.record_route_name_col, str)
        form['revenue'] = self.get_cell_value(row, self.record_revenue_col, float)
        form['cashier_name'] = self.get_cell_value(row, self.record_cashier_name_col, str)
        form['remnant_num'] = self.get_cell_value(row, self.record_remnant_col, int)
        form['remnant_value'] = self.get_cell_value(row, self.record_remnant_col + 1, float)
        form['fake_num'] = self.get_cell_value(row, self.record_fake_col, int)
        form['fake_value'] = self.get_cell_value(row, self.record_fake_col + 1, float)
        payment_form = self.get_payment_dict(row)
        form = {**form, **payment_form}
        m = Record.update_or_new(form, date=form['date'],
                                 car_name=form['car_name'],
                                 route_name=form['route_name'])
        m.update(form, hard=True)

        return m

    def get_payment_dict(self, row):
        # 遍历一行, 把建立PaymentType, Payment建立关系
        # 遍历一行, 把payment整理成dict返回, key是payment_name, value是[payment_num, payment_value]
        i = self.payment_start_col
        payment_form = {}
        payment_type_name = ''
        while i < self.payment_end_col:
            form = {}
            payment_name = self.sheet.cell_value(self.title_row, i)
            if payment_name == "合计":
                i += 2
                continue
            form['payment_name'] = str(payment_name)
            name = self.get_cell_value(self.payment_type_row, i, str)
            if name:
                form['payment_type_name'] = name
                payment_type_name = name
            else:
                form['payment_type_name'] = payment_type_name
            p = Payment.update_or_new(form, payment_name=payment_name)
            payment_form[payment_name] = [self.get_cell_value(row, i, int), self.get_cell_value(row, i + 1, float)]
            i += 2
        return payment_form

    def read_whole(self):
        for i in range(self.record_start_row, self.record_end_row):
            self.read_line(i)


if __name__ == '__main__':
    import os
    for i in os.listdir('xls'):
        a = Excel2Form('xls/' + i)
        a.read_whole()
        print('done  >>  ' + i)
    print ("all done")

