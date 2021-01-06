from models.record import Record
from statistics.statstic_tool import *


def aggregate(func):
    return Record.aggregate(func, 'car_name')


def get_output_form():
    res = {}
    res['营收现金'] = aggregate(revenue_sum)
    res['残币数量'] = aggregate(remnant_num_sum)
    res['残币金额'] = aggregate(remnant_value_sum)
    res['假币数量'] = aggregate(fake_num_sum)
    res['假币金额'] = aggregate(fake_value_sum)
    res['学生卡'] = aggregate(student_sum)
    res['敬老卡'] = aggregate(old_sum)
    res['普通卡'] = aggregate(common_sum)
    res['教师卡'] = aggregate(teacher_sum)
    res['优抚卡'] = aggregate(better_sum)
    res['异地卡'] = aggregate(offsite_sum)
    res['公务卡'] = aggregate(official_sum)
    res['银联二维码'] = aggregate(silver_qrcode_sum)
    res['银联双免'] = aggregate(silver_double_sum)
    res['银联ODA'] = aggregate(silver_oda_sum)
    res['天骄通二维码'] = aggregate(sky_qrcode_sum)
    return res


def write_out(output_form):
    import xlrd
    import xlwt
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('1')
    template = xlrd.open_workbook('../template.xls').sheet_by_index(0)

    for col in range(1, template.ncols):
        title = template.cell_value(0, col)
        worksheet.write(0, col, label=str(title))
    for row in range(1, template.nrows):
        car_name = template.cell_value(row, 0)
        worksheet.write(row, 0, label=str(car_name))
    # row = 1
    # a = list(output_form.values())[0]
    # for k, v in a.items():
    #     worksheet.write(row, 0, label=k)
    #     row += 1

    flag = 1
    col = 1
    while col < template.ncols:
        row = 1
        title = template.cell_value(0, col)
        while row < template.nrows:
            car_name = template.cell_value(row, 0)
            li = output_form.get(title, 0)
            if li:
                label = li.get(car_name, 0)
            else:
                label = 0

            if type(label) == tuple:
                flag = 0
                worksheet.write(row, col, label=label[0])
                worksheet.write(row, col+1, label=label[1])
            else:
                flag = 1
                worksheet.write(row, col, label=label)
            print(str(row) + '行' + str(col) + '列: ' + str(label))
            row += 1

        if flag:
            col += 1
        else:
            col += 2
            flag = 1

    workbook.save('单车营收汇总.xls')


def output():
    a = get_output_form()
    write_out(a)


if __name__ == '__main__':
    output()