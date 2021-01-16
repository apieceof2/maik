import xlrd


def open_excel(filename):
    sheet = xlrd.open_workbook(filename).sheet_by_index(0)
    return sheet
