from statistics.routes.expend_routes.sheet1_table1 import ExpendSheet1Table1
from statistics.routes.expend_routes.sheet2_table1 import ExpendSheet2Table1
from statistics.routes.expend_routes.sheet3_table1 import ExpendSheet3Table1
from statistics.routes.expend_routes.sheet4_table1 import ExpendSheet4Table1
from statistics.routes.expend_routes.sheet5_table1 import ExpendSheet5Table1
from statistics.routes.expend_routes.sheet6_table1 import ExpendSheet6Table1
from statistics.routes.expend_routes.sheet7_table1 import ExpendSheet7Table1
from statistics.routes.expend_routes.sheet8_table1 import ExpendSheet8Table1
from statistics.routes.expend_routes.sheet9_table1 import ExpendSheet9Table1
from statistics.routes.expend_routes.sheet10_table1 import ExpendSheet10Table1
from statistics.routes.expend_routes.sheet11_table1 import ExpendSheet11Table1
from statistics.routes.expend_routes.sheet12_table1 import ExpendSheet12Table1
from statistics.routes.expend_routes.sheet13_table1 import ExpendSheet13Table1
from statistics.routes.expend_routes.sheet14_table1 import ExpendSheet14Table1


def routes_mapping(signature):
    t = signature.split('?')
    print(t)
    name = t[0]
    if len(t) > 1:
        key = t[1].split('=')[0]
        value = t[1].split('=')[1]
        arg = {key: value}
        return ROUTES_MAPPING[name](**arg)
    else:
        return ROUTES_MAPPING[name]()

ROUTES_MAPPING = {
    # 第一个表不同油类型
    'sheet1_table1': ExpendSheet1Table1,
    'sheet2_table1': ExpendSheet2Table1,
    'sheet3_table1': ExpendSheet3Table1,
    'sheet4_table1': ExpendSheet4Table1,
    'sheet5_table1': ExpendSheet5Table1,
    'sheet6_table1': ExpendSheet6Table1,
    'sheet7_table1': ExpendSheet7Table1,
    'sheet8_table1': ExpendSheet8Table1,
    'sheet9_table1': ExpendSheet9Table1,
    'sheet10_table1': ExpendSheet10Table1,
    'sheet11_table1': ExpendSheet11Table1,
    'sheet12_table1': ExpendSheet12Table1,
    'sheet13_table1': ExpendSheet13Table1,
    'sheet14_table1': ExpendSheet14Table1,
}
