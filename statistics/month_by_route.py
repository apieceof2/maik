from models.record import Record
from statistics.statstic_tool import *
from statistics.statstic_tool import _count
from statistics.statstic_tool import _sum


def aggregate(func):
    return Record.aggregate(func, 'route_name')



def card_num(q):
    return _sum(q, '实体卡（IC卡）_num__sum')

def card_value(q):
    return _sum(q, '实体卡（IC卡）_value__sum')

def silver_num(q):
    return _sum(q, '银联+天交通二维码_num__sum')

def silver_value(q):
    return _sum(q, '银联+天交通二维码_value__sum')



def get_output_form():
    form = {}
    form['路线车辆数'] = aggregate(_count)
    form['营收现金'] = aggregate(revenue_sum)
    form['实体卡（IC卡）_num__sum'] = aggregate(card_num)
    form['实体卡（IC卡）_value__sum'] = aggregate(card_value)
    form['银联+天交通二维码_num__sum'] = aggregate(silver_num)
    form['银联+天交通二维码_value__sum'] = aggregate(silver_value)
    print(form['路线车辆数'])
    return form


def write_out(output_form):
    import xlrd
    import xlwt
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('1')
    template = xlrd.open_workbook('../template_route.xls').sheet_by_index(0)

    for col in range(1, template.ncols):
        title = template.cell_value(0, col)
        worksheet.write(0, col, label=str(title))
    for row in range(1, template.nrows):
        car_name = template.cell_value(row, 0)
        worksheet.write(row, 0, label=str(car_name))

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

    workbook.save('月营收总汇.xls')

if __name__ == '__main__':
    a = get_output_form()
    write_out(a)



