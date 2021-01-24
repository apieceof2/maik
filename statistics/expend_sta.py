from statistic import Statistic


class ExpendSta(Statistic):
    def __init__(self, template_path, duration=None):
        super(ExpendSta, self).__init__(template_path, duration=duration)
        from statistics.routes.expend_routes.routes import ROUTES_MAPPING
        self.routes = ROUTES_MAPPING


if __name__ == '__main__':
    duration = ('2021.01.01', '2021.01.02')
    i = ExpendSta('sheet9_table1', duration=duration)
    i._output_sheet()
