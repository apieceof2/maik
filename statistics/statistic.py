import os
import xlutils.copy
import xlrd
import xlwt


class Statistic:
    """
    这是一个基类, 继承的子类根据自己的类名查找template文件, 通过template生成文件
    """

    def __init__(self, signature, duration=None):
        """
        :param signature: a str, like "sheet_template_name?key=value"
        :param duration:
        """

        self.table_name = signature
        self.config = self._get_config()
        template_path = os.path.join(self.config.get('json_path'), self.table_name.split('?')[0] + '.json')
        self.template = self._get_templates(template_path)
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

        # 时间区间
        self.duration = duration

        # 获得routes
        from statistics.routes.routes_mapping import routes_mapping
        self.routes = routes_mapping

    @classmethod
    def _get_templates(cls, template_path):
        """
        根据类名获得templates
        :return: templates
        """
        import json
        with open(template_path, encoding='utf-8') as f:
            template = json.load(f)
            return template

    @classmethod
    def _get_config(cls):
        """
        根据类名获得config
        :return:
        """
        from statistics.config import CONFIG_DISPATCHER
        return CONFIG_DISPATCHER[cls.__name__]

    def _get_data(self, table_name, row_number=False):
        """
        根据类名, sheet名取得获得数据的方法并返回
        :type row_number: bool
        :param row_number:
        :param table_name: template中一个sheet_name的名称
        :return: 一个方法, 用于获得数据
        """
        data = self.routes(table_name)(row_number=row_number, duration=self.duration)
        return data

    def output_sheet(self):
        """
        把数据输出到一个表中
        """

        # 查看文件夹是否存在, 如果没有则新建
        filepath = os.path.join(self.output_path, self.filename)
        if not os.path.exists(self.output_path):
            os.mkdir(self.output_path)

        # 通过sheet_name获得template
        template = self.template

        # 通过template中的信息, 查看sheet是否存在, 如果存在, 设置offset
        # 否则, 新建一个sheet 设置offset = 0
        sheet_name = template.get('sheet_name')
        offset = 0
        sheet = None

        try:
            book = xlrd.open_workbook(self.filepath, formatting_info=True)
            if book:
                self.output_book = xlutils.copy.copy(book)
                sheet = book.sheet_by_name(sheet_name)
                offset = sheet.nrows + 2
                sheet = self.output_book.get_sheet(sheet_name)
        except:
            sheet = self.output_book.add_sheet(sheet_name)
            offset = 0

        # 将template中的数据写入sheet
        # 合并表头
        for merge in template.get('merges'):
            sheet.merge(merge[0] + offset, merge[1] + offset, merge[2], merge[3])
        # 写入表头
        for title in template.get('titles'):
            sheet.write(title[0] + offset, title[1], title[2], self.style)

        # 获得变量数据
        data = self._get_data(self.table_name, row_number=template.get('row_number'))
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

