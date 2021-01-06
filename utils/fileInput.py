import os
from excel import Excel2Form


if __name__ == '__main__':
    print(os.listdir('xls'))
    for i in os.listdir('xls'):
        a = Excel2Form('xls/' + i)
        a.upload()
        print(i + " > done")
    print('done')