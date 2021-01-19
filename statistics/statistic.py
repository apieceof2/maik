from abc import abstractmethod
from logging import exception

from Config import STATISTIC_DISPATCH
from Config import config
from datetime import datetime
import xlwt
import os
from xlutils.copy import copy


class Statistic:
    def __init__(self):
        self.filename = self._get_filename()
        self.template_path = os.path.join(config.get('TEMPLATES_DIR'), self.filename)
        self.output_path = os.path.join(config.get('OUTPUT_DIR'), self.filename)
        self.templates = xlrd.open_workbook(self.template_path, formatting_info=True)
        self.output = copy(self.templates)

        self.style = xlwt.XFStyle()
        al = xlwt.Alignment()
        al.horz = 0x02
        al.vert = 0x01
        self.style.alignment = al

        # 创建excel
        self.workbook = xlwt.Workbook(encoding='utf-8')

    @classmethod
    def _get_filename(cls):
        """通过config找到这个类对应的template文件, 返回文件名
        :return: 这个类对应的文件名
        :rtype: str
        """

        return STATISTIC_DISPATCH.get(cls.__name__, str(datetime.now()))

    @abstractmethod
    def get_data(self, name):
        # 获得一个表格的数据
        # param name: filename + sheet_name
        # return list, 其中的元素是三元组, (row, col, value)
        pass

    @classmethod
    def _get_template_info(cls, t):
        """在模板中找到控制信息并返回

        :param t: 模板
        :return: 一个字典, 包括
                file_name: 输出文件名
                sheet_name: 输出的sheet名
                start_row: 数据输出的起始行
        :rtype: dict
        """
        # param t: 一个sheet格式的模板文件
        # 功能: 从模板文件中找到控制信息返回
        ctrl_row = template.nrows - 1
        file_name = str(t.cell_value(ctrl_row, 0))
        sheet_name = str(t.cell_value(ctrl_row, 1))
        start_row = int(t.cell_value(ctrl_row, 2))

        if not file_name:
            file_name = str(datetime.now())
        if not sheet_name:
            sheet_name = str(datetime.now())
        if not start_row:
            start_row = 0

        f = dict(
            file_name=file_name,
            sheet_name=sheet_name,
            start_row=start_row,
        )
        return f

    def output_file(self):
        """查找所有的模板, 并对每个模板进行输出
        """
        for t in self.templates:
            self.output_table(t)

    def output_table(self, t):
        """获得一个template, 将这个template复制到输出目录， 并在这个文件中输出数据
        :param t: 输出的模板
        """

        # 从template中获得template_info
        template_info = self._get_template_info(t)

        # 找到对应的sheet
        sheet = self.output.get_sheet(t.name)

        # 通过filename + sheet_name获得数据
        name = template_info.get('file_name') + ':' + template_info.get('sheet_name')
        data = self.get_data(name)

        # 数据写入sheet
        if data:
            for item in data:
                print(data)
                sheet.write(item[0], item[1], label=item[2])

        self._save(file_name=template_info.get('file_name', self.filename))

    def _save(self, file_name):
        self.output.save(file_name)



if __name__ == '__main__':
    a = Statistic()
    import xlrd
    template = xlrd.open_workbook('data_templates/test.xls').sheets()[0]
    a = Statistic()
    a.output_table(template)