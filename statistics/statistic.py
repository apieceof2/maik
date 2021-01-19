import os
import xlutils.copy
import xlrd
import xlwt


class Statistic:
    """
    这是一个基类, 继承的子类根据自己的类名查找template文件, 通过template生成文件
    """
    def __init__(self):
        self.config = self._get_config()
        self.templates = self._get_templates()
        self.filename = self.__class__.__name__ + '.xls'
        self.output_path = self.config.get('output_path')
        self.filepath = os.path.join(self.output_path, self.filename)

        # 空文件, 用于xlutils 复制
        empty = xlrd.open_workbook(self.config.get('empty_path'))
        self.output_book = xlutils.copy.copy(empty)

        # style
        self.style = xlwt.XFStyle()
        self.style.alignment.horz = 0x02
        self.style.alignment.vert = 0x01



    @classmethod
    def _get_templates(cls):
        """
        根据类名获得templates
        :return: templates
        """
        from config import TEMPLATE_DISPATCHER
        return TEMPLATE_DISPATCHER[cls.__name__]

    @classmethod
    def _get_config(cls):
        """
        根据类名获得config
        :return:
        """
        from config import CONFIG_DISPATCHER
        return CONFIG_DISPATCHER[cls.__name__]

    def get_data(self, sheet_name):
        """
        根据类名, sheet名取得获得数据的方法并返回
        :param sheet_name: template中一个sheet_name的名称
        :return: 一个方法, 用于获得数据
        """
        # 这个函数要在子类中重写, 这里用作测试
        data = {
            'vars': {
                'duration': '2020-2012'
            },
            'data': [
                (0, 0, 1),
                (0, 1, 2),
                (0, 2, 3),
                (0, 3, 4),
                (0, 4, 4),
                (0, 5, 5),
                (0, 6, 6)
            ]
        }

        return data

    def _output_sheet(self, sheet_index, data):
        """
        把数据输出到一个表中
        :param sheet_index: int 表格所在的sheet的序号
        :param data: 这个表格的数据 是一个list, 其中是三元组(row, col, value)
        """

        # 查看文件夹是否存在, 如果没有则新建
        filepath = os.path.join(self.output_path, self.filename)
        if not os.path.exists(self.output_path):
            os.mkdir(self.output_path)

        # 通过sheet_name获得template
        template = self.templates[sheet_index]

        # 通过template中的信息, 查看sheet是否存在, 如果存在, 设置offset
        # 否则, 新建一个sheet 设置offset = 0
        sheet_name = template.get('name')
        offset = 0
        sheet = None

        try:
            book = xlrd.open_workbook(self.filepath, formatting_info=True)
            if book:
                self.output_book = xlutils.copy.copy(book)
                sheet = book.sheet_by_name(sheet_name)
                offset = sheet.nrows + 2
                sheet = self.output_book.get_sheet(sheet_name)
        except :
            sheet = self.output_book.add_sheet(sheet_name)
            offset = 0

        # 将template中的数据写入sheet
        # 合并表头
        for merge in template.get('merges'):
            sheet.merge(merge[0] + offset, merge[1] + offset, merge[2], merge[3])
        # 写入表头
        for title in template.get('titles'):
            sheet.write(title[0] + offset, title[1], title[2], self.style)

        # 获得数据
        data = self.get_data(sheet_name)
        data_offset = offset + template.get('start_row')
        # 写入变量
        vars = data['vars']
        for key, value in vars.items():
            row = template['vars'][key][0]
            col = template['vars'][key][1]
            sheet.write(offset + row, col, value, self.style)
        # 写入数据
        data = data['data']
        for cell in data:
            sheet.write(data_offset + cell[0], cell[1], cell[2], self.style)

        self.output_book.save(self.filepath)
        print(self.filename + " : " + sheet_name + ' >>> done')

    def output_sheet_by_name(self, sheet_name):
        """
        通过 sheet_name 导出文件
        :param sheet_name:
        """
        data = self.get_data(sheet_name)
        index = -1
        for template_index in range(0, len(self.templates)):
            if self.templates[template_index].get('name') == sheet_name:
                index = template_index
        if index == -1:
            raise Exception(print('没有这个sheet'))
        else:
            self._output_sheet(index, data)

    def output_sheet_by_index(self, index):
        """
        通过index导出文件
        :param index:
        :return:
        """
        if index > len(self.templates) - 1:
            raise Exception(print("没有这个sheet(超出范围)"))
        else:
            sheet_name = self.templates[index].get('name')
            data = self.get_data(sheet_name)
            self._output_sheet(index, data)

    def output_all(self):
        """
        导出templates中所有template代表的文件
        :return:
        """

        # 删除导出目录中的表
        files = os.listdir(self.config.get('output_path'))
        for file in files:
            filepath = os.path.join(self.config.get('output_path'), file)
            os.remove(filepath)

        for index in range(0, len(self.templates)):
            self.output_sheet_by_index(index)


if __name__ == '__main__':
    a = Statistic()
    a.output_sheet_by_index(0)












