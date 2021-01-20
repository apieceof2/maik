class Route:
    def __init__(self):
        self.data = {
            'vars': {
                'duration': '2012'
            },
            'data': []
        }
        from models.mongo import Mongo
        self.DB = Mongo
        self.aggregation_key = 'route'

    def _get_data(self, duration=None):
        """
        获得
        :param self:
        :param duration:
        :return:
        """
        # 获得聚合
        q = self.DB.aggregate(self._aggregation_func, self.aggregation_key, duration)

        # 聚合结果变为三元组
        res = []
        row = 0
        for key, values in q.items():
            col = 0
            for v in values:
                res.append((row, col, v))
        return res


    @staticmethod
    def _aggregation_func(q):
        """
        聚合用的函数, 子类重写
        :param q:
        :return:
        """
        return [len(q)]

    def __call__(self, add_number=False, duration=None):
        """
        返回数据, 如果需要则加入序号
        :param add_number:
        :param args:
        :param kwargs:
        :return:
        """
        self.data['data'] = self._get_data(duration)
        if add_number:
            self.add_number()
        return self.data

    def add_number(self):
        """
        给self.data['data']的所有项目第一行加上序号
        :return:
        """
        row = 0
        data = []

        # 找到data中最大的row, 并使所有三元组向后移动一列
        for i in self.data['data']:
            data.append((i[0], i[1] + 1, i[2]))
            if i[0] > row:
                row = i[0]

        # 添加行号
        for i in range(0, row + 1):
            data.append((i, 0, i + 1))

        self.data['data'] = data
