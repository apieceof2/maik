from statistics.statistic import Statistic


class IncomeSta(Statistic):
    def __init__(self, template_path, duration=None):
        super(IncomeSta, self).__init__(template_path, duration=duration)
        from statistics.routes.income_routes.routes import routes_mapping
        self.routes = routes_mapping
