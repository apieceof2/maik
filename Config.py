INCOME_CONFIG = dict(
    START_ROW=5,
    PAYMENT_TYPE_ROW=2,
    PAYMENT_START_COL=15,
    CAR_COL=1,
    ROUTE_COL=2,
    REVENUE_COL=3,
    CASHIER_COL=4,
    REMNANT_COL=5,
    FAKE_COL=7,
    PEOPLE_NUM_BY_CASH_COL=10,
    PEOPLE_NUM_BY_CAL_COL=13,
    PEOPLE_NUM_BY_CAR_COL=14,
    TITLE_ROW=3,
    DATE_ROW=1,
)

EXPEND_CONFIG = dict(
    START_ROW=5,
    CAR_COL=1,
    ROUTE_COL=2,
    RESOURCE_TYPE_ROW=2,
    RESOURCE_ROW=3,
    RESOURCE_START_COL=3,
    DATE_ROW=1,
    TITLE_ROW=3,
)

TEST_CONFIG = dict(
    START_ROW=5,
    CAR_NAME_COL=1,
    ROUTE_NAME_COL=2,
    RESOURCE_TYPE_COL=3,
    DATE_ROW=1,
    DATE_COL=0,
    TITLE_ROW=3,
)

STATISTIC_DISPATCH = dict(
    Statistic="test.xls"

)

config = {
    'Income2Form': INCOME_CONFIG,
    'Expend2Form': EXPEND_CONFIG,
    'ToForm': TEST_CONFIG,
    'OUTPUT_DIR': 'output',
    'TEMPLATES_DIR': 'data_templates',
}
