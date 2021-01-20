from data_templates.test_templates import templates as test
from data_templates.income_templates import templates as income

test_config = {
    "output_path": 'output',
    'empty_path': 'empty.xls'
}

income_config = {
    "output_path": 'output',
    'empty_path': 'empty.xls'
}

TEMPLATE_DISPATCHER = {
    'Statistic': test,
    'IncomeSta': income
}

CONFIG_DISPATCHER = {
    'Statistic': test_config,
    'IncomeSta': income_config
}
