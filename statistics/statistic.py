from abc import abstractmethod
from Config import STATISTIC_DISPATCH
from Config import config
from datetime import datetime
import xlwt
import os


class Statistic:
    def __init__(self):
        self.filename = self.get_filename()

        # 创建excel
        self.workbook = xlwt.Workbook(encoding='utf-8')

    @classmethod
    def get_filename(cls):
        # 通过类名找到Config中对应的文件名
        # 这个文件名既是模板名， 又是输出名
        return STATISTIC_DISPATCH.get(cls.__name__, str(datetime.now()))

    @abstractmethod
    def get_data(self, name):
        # 获得一个表格的数据
        # param name: filename + sheet_name
        pass

    def get_template_info(self, template):
        # 从一个template中获得基本信息
        # filename：当前文件名
        # start： 从第一行开始为正式信息
        # sheet_name: 当前sheet名
        filename = str(template.cell_value(0, 0))
        start = int(template.cell_value(0, 1))
        sheet_name = str(template.cell_value(0, 2))
        if not filename:
            filename = str(datetime.now())
        if not start:
            start = 0
        if not sheet_name:
            sheet_name = str(datetime.now())

        return dict(
            filename=filename,
            start=start,
            sheet_name=sheet_name,
        )

    def output_file(self):
        # 访问这个文件中的所有template，（template中有关于
        import xlrd
        filename = os.path.join(config.get('TEMPLATES_DIR'), self.filename)
        filepath = os.path.join(os.getcwd(), filename)
        templates = xlrd.open_workbook(filepath).sheets()
        for template in templates:
            self.output_table(template)

    def output_table(self, template):
        # 获得一个template, 将这个template复制到输出目录， 并在这个文件中输出数据

        # 从template中获得template_info
        template_info = self.get_template_info(template)

        # 新建一个sheet
        sheet = self.workbook.add_sheet(template_info.get('sheet_name', str(datetime.now())))

        # 复制这个template到sheet
        for row in range(1, template_info.get('start', 0)):
            for col in range(0, template.ncols):
                value = template.cell_value(row, col)
                sheet.write(row - 1, col, label=value)

        # 通过filename + sheet_name获得数据
        name = template_info.get('filename') + ':' + template_info.get('sheet_name')
        data = self.get_data(name)

        # 将数据写入sheet
        row = template_info.get('start', 0) - 1
        data = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                [1, 2, 3, 4, 5, 6]]
        # test
        if data:
            for line in data:
                col = 0
                for value in line:
                    sheet.write(row, col, label=value)
                    col += 1
                row += 1

        # 保存数据
        filepath = config.get('OUTPUT_DIR') + template_info.get('filename')
        print(filepath)
        self.workbook.save(filepath)


if __name__ == '__main__':
    a = Statistic()
    a.output_file()
