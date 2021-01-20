from statistic import Statistic

from routes.income_routes import *


class IncomeSta(Statistic):
    def __init__(self):
        super(IncomeSta, self).__init__()


if __name__ == '__main__':
    i = IncomeSta()
    i.output_sheet_by_index(0)
