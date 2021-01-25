from xls_loader.income2form import Income2Form
from xls_loader.expend2form import Expend2Form


def load_income_xls():
    import os

    # 导入所有income
    income_xls_list = os.listdir('files/income_xls/')
    for i in income_xls_list:
        a = Income2Form(i)
        a.read_page()
        print(i, end='')
        print(" >>> 已经被导入数据库")
    for i in income_xls_list:
        os.remove('files/income_xls/'+i)

def load_expend_xls():
    import os
    expend_xls_list = os.listdir('files/expend_xls/')
    for i in expend_xls_list:
        a = Expend2Form(i)
        a.read_page()
        print(i, end='')
        print(" >>> 已经被导入数据库")
    for i in expend_xls_list:
        os.remove('files/expend_xls/'+i)


