import xlrd
import xlutils.copy
import os
import xlwt

def test():
    path = os.path.join(os.getcwd(), 'test.xls')
    print(path)
    old_f = xlrd.open_workbook(path, formatting_info=True)
    new_f = xlutils.copy.copy(old_f)

    old_sheet = old_f.sheets()[1]
    new_sheet = new_f.get_sheet(1)

    style = xlwt.XFStyle()
    al = xlwt.Alignment()
    al.horz = 0x02
    al.vert = 0x01
    style.alignment = al
    for row in range(0, old_sheet.nrows):
        for col in range(0, old_sheet.ncols):
            v = old_sheet.cell(row, col).value
            if v:
                print(v)
            new_sheet.write(row + 19, col, label=v)
    new_sheet.write(0, 0, 'hahah',style=style)
    new_f.save('test2.xls')



if __name__ == '__main__':
    test()