from statistic import Statistic


class IncomeSta(Statistic):
    def __init__(self, template_path, duration=None):
        super(IncomeSta, self).__init__(template_path, duration=duration)
        from statistics.routes.income_routes.routes import ROUTES_MAPPING
        self.routes = ROUTES_MAPPING


if __name__ == '__main__':
    duration = ('2021.01.02', '2021.01.02')
    i = IncomeSta('sheet6_table1.json', duration=duration)
    i._output_sheet()
