import xlrd

def get_value(sheet):
    """
    从sheet中获得所有单元格的数据组成元组(row, col, value), 然后元组组成list, str输出到一个txt中
    :param sheet: xlrd.Workbook.sheet
    :return: list
    """
    l = []
    for row in range(0, sheet.nrows):
        for col in range(0, sheet.ncols):
            l.append((row, col, sheet.cell_value(row, col)))
    print(str(l))

    with open('sheet/' + sheet.name + '.txt', 'w') as f:
        for t in l:
            if t[2]:
                f.write(str(t) + ',\r')


def get_book():
    filename = '../../../income.xls'
    sheets = xlrd.open_workbook(filename).sheets()
    for s in sheets:
        get_value(s)


if __name__ == '__main__':
    get_book()

