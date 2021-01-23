from abc import ABC

from models.expend import Expend
from models.resource import Resource
from .toForm import ToForm


class Expend2Form(ToForm, ABC):
    def __init__(self, filename):
        super(Expend2Form, self).__init__(filename)
        if not getattr(self, 'resource_end_col', 0):
            setattr(self, 'resource_end_col', self.get_resource_end_col())

    # 获得资源类型最后一行的行数
    def get_resource_end_col(self):
        return self.sheet.ncols - 1

    def read_line(self, row):
        # 功能: 读入某一行的记录, 然后载入到数据库中
        # params row: 行号

        # 基本数据
        basic_form = {
            'date': self.get_cell_value(getattr(self, 'date_row'), 0, t=str),
            'car': self.get_cell_value(row, getattr(self, 'car_col'), t=str),
            'route': self.get_cell_value(row, getattr(self, 'route_col'), t=str),
        }
        # resource的数据
        resource_form = {}

        # 把Resource和ResourceType关系建立起来并加入Expend
        resource_type_row = getattr(self, 'resource_type_row')
        resource_start_col = getattr(self, 'resource_start_col')
        resource_end_col = getattr(self, 'resource_end_col')
        title_row = getattr(self, 'title_row')
        resource_type_name = ''
        title_name = ''
        fields = []  # 这个用来把某一个支付手段下所有字段保存起来, 最后放在Resource里
        flag = 0  # 用来记录是不是第一个title
        for col in range(resource_start_col, resource_end_col):
            # 遍历, 如果有新的title, 设置title_name, 然后开始记录fields直到下一个
            # title出现, 这个时候将已经积累的title载入数据库
            title = self.get_cell_value(title_row, col, t=str)
            resource_type = self.get_cell_value(resource_type_row, col, t=str)
            if title:
                resource_form[title] = []
                if flag == 0:
                    title_name = title
                    flag = 1
                elif flag == 1:
                    f = dict(name=title_name,
                             resource_type=resource_type_name,
                             fields=tuple(fields), )
                    Resource.update_or_new(f, name=title_name,
                                           resource_type=resource_type_name)
                    fields = []
                    title_name = title
            if resource_type:
                resource_type_name = resource_type
            temp = self.get_cell_value(title_row + 1, col, t=str)
            if temp:
                fields.append(temp)
            temp = self.get_cell_value(row, col)
            if temp:
                resource_form[title_name].append(temp)
        # 把最后一个加上
        f = dict(name=title_name,
                 resource_type=resource_type_name,
                 fields=tuple(fields), )
        Resource.update_or_new(f, name=title_name,
                               resource_type=resource_type_name)

        f = {**basic_form, **resource_form}
        Expend.update_or_new(f,
                             date=f['date'],
                             car=f['car'],
                             route=f['route'])


