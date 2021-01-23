from abc import abstractmethod, ABCMeta
import xlrd
import os


def open_excel(filename):
    sheet = xlrd.open_workbook(filename).sheet_by_index(0)
    return sheet


class ToForm:
    __metaclass__ = ABCMeta

    @classmethod
    def get_config(cls):
        # 用类名将config载入
        from .config import config
        config = config.get(cls.__name__, None)
        if config:
            return config
        else:
            pass
            # todo: 这里检错

    def __init__(self, filename):

        # 将设置中的参数载入init
        config = self.get_config()
        for key, value in config.items():
            setattr(self, str.lower(key), value)

        # 打开文件
        filepath = getattr(self, 'load_path')
        filepath = os.path.join(filepath, filename)
        self.sheet = open_excel(filepath)

        # 确定有start_row 和 end_row
        start = getattr(self, 'start_row', 0)
        if not start:
            setattr(self, 'start_row', 0)

        end = getattr(self, 'end_row', 0)
        if not end:
            setattr(self, 'end_row', self.get_end_row())



    def get_cell_value(self, row, col, t=None):
        # 获得这张表row行, col列的数据,并且保证type为t, 转型
        a = self.sheet.cell_value(row, col)
        if a:
            if t:
                return t(a)
            else:
                return a
        else:
            return None

    @abstractmethod
    def read_line(self, row):
        # 功能: 读入某一行的记录, 然后载入到数据库中
        # params row: 行号
        pass

    @abstractmethod
    def get_end_row(self):
        # 获得记录的最后一行, 默认是第一个以下条件的行的行数: 第二列为空的行
        row = getattr(self, 'start_row')
        while self.sheet.cell_value(row, 1):
            row += 1
        return row

    def read_page(self):
        # 将整整一张表载入数据库
        for row in range(getattr(self, 'start_row', 0), getattr(self, 'end_row', 0)):
            self.read_line(row)

    @staticmethod
    def strip_space(s):
        res = ""
        if s:
            l = s.split(' ')
            for i in l:
                res += i
        return res







