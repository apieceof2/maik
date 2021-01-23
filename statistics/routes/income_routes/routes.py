from statistics.routes.income_routes.sheet1_table1 import IncomeSheet1Table1
from statistics.routes.income_routes.sheet1_table2 import IncomeSheet1Table2
from statistics.routes.income_routes.sheet2_table1 import IncomeSheet2Table1
from statistics.routes.income_routes.sheet2_table2 import IncomeSheet2Table2
from statistics.routes.income_routes.sheet2_table3 import IncomeSheet2Table3
from statistics.routes.income_routes.sheet3_table1 import IncomeSheet3Table1
from statistics.routes.income_routes.sheet4_table1 import IncomeSheet4Table1
from statistics.routes.income_routes.sheet5_table1 import IncomeSheet5Table1
from statistics.routes.income_routes.sheet6_table1 import IncomeSheet6Table1


ROUTES_MAPPING = {
    'sheet1_table1': IncomeSheet1Table1('sheet1_table1'),
    'sheet1_table2': IncomeSheet1Table2('sheet1_table2'),
    'sheet2_table1': IncomeSheet2Table1('sheet2_table1'),
    'sheet2_table2': IncomeSheet2Table2('sheet2_table2'),
    'sheet2_table3': IncomeSheet2Table3('sheet2_table3'),
    'sheet3_table1': IncomeSheet3Table1('sheet3_table1'),
    'sheet4_table1': IncomeSheet4Table1('sheet4_table1'),
    'sheet5_table1': IncomeSheet5Table1('sheet5_table1'),
    'sheet6_table1': IncomeSheet6Table1('sheet6_table1'),
}

