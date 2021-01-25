from statistics.statistic import Statistic


class ExpendSta(Statistic):
    def __init__(self, signature, duration=None):
        super(ExpendSta, self).__init__(signature, duration=duration)
        from statistics.routes.expend_routes.routes import routes_mapping
        self.routes = routes_mapping

