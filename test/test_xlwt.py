import xlwt


def test():
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('bc')

    worksheet.write(1, 0, label='hshs')
    workbook.save("haha.xls")


if __name__ == '__main__':
    test()