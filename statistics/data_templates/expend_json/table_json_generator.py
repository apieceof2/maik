from models.income import Income


def get_routes():
    # 获得所有的 route, 然后组成三元组输出
    def func(q):
        return []

    routes = []
    i = 1
    for item in Income.aggregate(func, 'route'):
        tri = [2, i, item]
        routes.append(tri)
        i += 2
    print(routes)


def get_cells(file_path, index, start_row=-1, end_row=-1, start_col=-1, end_col=-1):
    """
    finds cells limited in row and col in a excel file
    and returns their values with coordinate in a list
    like[(row, col, value),]
    :param start_row:
    :param index: the index of the sheets in a excel document
    :param file_path: the .xls file path
    :return: a list of values of all cell
    """
    # open the file
    import xlrd
    file = xlrd.open_workbook(file_path)
    sheet = file.sheet_by_index(index)
    print(sheet.name)

    # traverse all the cell in this sheet , and make the (row, col, value)
    if start_row == -1:
        start_row = 0
    if start_col == -1:
        start_col = 0
    if end_col == -1:
        end_cols = sheet.ncols
    if end_row == -1:
        end_rows = sheet.nrows

    res = []
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            value = sheet.cell_value(row, col)
            if value:
                data = [row, col, sheet.cell_value(row, col)]
                res.append(data)
    for i in res:
        print('[', end='')
        for value in i:
            if type(value) == str:
                print('"' + value + '"', end='')

            else:
                print(value, end='')
                print(',', end='')
        print('],')


def sheet2_table1_merge():
    res = [
        [0, 0, 0, 29],
        [1, 1, 0, 29],
    ]

    for i in range(1, 29, 2):
        merge = [2, 2, i, i + 1]
        res.append(merge)
    print(res)


def sheet2_table2_merge():
    res = [
        [0, 0, 0, 29],
        [1, 1, 0, 29],
        [2, 3, 1, 1],
        [9, 9, 0, 1],
        [10, 10, 0, 1],
        [11, 11, 0, 1],
    ]
    for i in range(1, 39, 2):
        merge = [2, 2, i, i + 1]
        res.append(merge)
    print(res)


def sheet3_table1_merge():
    res = [[0, 0, 0, 20],
           [1, 1, 0, 20],
           [2, 3, 0, 0],
           [2, 3, 1, 1],
           [2, 3, 2, 2],
           [3, 3, 3, 4],
           ]
    for i in range(3, 19, 2):
        data = [2, 2, i, i + 1]
        res.append(data)
    print(res)


def sheet7_table1_merge():
    res = [
        [0, 0, 0, 22],
        [1, 1, 0, 22],
        [2, 2, 0, 1],
        [2, 2, 3, 4],
        [2, 2, 10, 16],
        [2, 2, 17, 20],
        [3, 4, 0, 0],
        [3, 4, 1, 1],
        [3, 4, 2, 2],
        [3, 4, 3, 3],
        [3, 4, 4, 4],
        [3, 4, 5, 5],
    ]

def sheet8_table1_merge():
    res = [
        [0, 0, 0, 21],
        [1, 1, 0, 21],
        [2, 2, 0, 1],
        [2, 2, 2, 3],
        [2, 2, 9, 15],
        [2, 2, 16, 19],
        [3, 4, 0, 0],
        [3, 4, 1, 1],
        [3, 4, 2, 2],
        [3, 4, 3, 3],
        [3, 4, 4, 4],
    ]


def sheet9_table1_merge():
    res = [
        [0, 0, 0, 20],
        [1, 1, 0, 20],
        [2, 2, 8, 14],
        [2, 2, 15, 18],
        [3, 4, 0, 0],
        [3, 4, 1, 1],
        [3, 4, 2, 2],
        [3, 4, 3, 3]
    ]


if __name__ == '__main__':
    get_cells("C:/Users/Administrator/Desktop/expense.xls", 6,
              start_row=0, end_row=3, start_col=0, end_col=4)
    # sheet3_table1_merge()
