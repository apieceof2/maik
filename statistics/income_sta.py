from statistic import Statistic

from routes.income_routes import *


class IncomeSta(Statistic):
    def __init__(self, add_number=False):
        super(IncomeSta, self).__init__()
        self.add_number = add_number


if __name__ == '__main__':
    i = IncomeSta(add_number=True)
    i.output_sheet_by_index(0)
