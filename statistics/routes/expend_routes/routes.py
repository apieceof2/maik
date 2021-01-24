from statistics.routes.expend_routes.sheet1_table1 import ExpendSheet1Table1
from statistics.routes.expend_routes.sheet2_table1 import ExpendSheet2Table1
from statistics.routes.expend_routes.sheet3_table1 import ExpendSheet3Table1
from statistics.routes.expend_routes.sheet4_table1 import ExpendSheet4Table1
from statistics.routes.expend_routes.sheet5_table1 import ExpendSheet5Table1
from statistics.routes.expend_routes.sheet6_table1 import ExpendSheet6Table1
from statistics.routes.expend_routes.sheet7_table1 import ExpendSheet7Table1
from statistics.routes.expend_routes.sheet8_table1 import ExpendSheet8Table1
from statistics.routes.expend_routes.sheet9_table1 import ExpendSheet9Table1

ROUTES_MAPPING = {
    # 第一个表不同油类型
    'sheet1_table1?gus_type=20#': ExpendSheet1Table1('20#'),
    'sheet1_table1?gus_type=35#': ExpendSheet1Table1('35#'),
    'sheet1_table1?gus_type=10#': ExpendSheet1Table1('10#'),
    # todo:把gus_type从签名中扒出来


    'sheet2_table1?gus_type=20#': ExpendSheet2Table1('20#'),
    'sheet2_table1?gus_type=35#': ExpendSheet2Table1('35#'),
    'sheet2_table1?gus_type=10#': ExpendSheet2Table1('10#'),

    'sheet3_table1?gus_type=20#': ExpendSheet3Table1('20#'),
    'sheet3_table1?gus_type=35#': ExpendSheet3Table1('35#'),
    'sheet3_table1?gus_type=10#': ExpendSheet3Table1('10#'),

    'sheet4_table1?car=蒙K90193': ExpendSheet4Table1('蒙K90193'),

    'sheet5_table1?car=蒙K90193': ExpendSheet5Table1('蒙K90193'),

    'sheet6_table1?car=蒙K90193': ExpendSheet6Table1('蒙K90193'),

    'sheet7_table1': ExpendSheet7Table1(),
    'sheet8_table1': ExpendSheet8Table1(),
    'sheet9_table1': ExpendSheet9Table1(),
}
