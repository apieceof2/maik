from data_templates.test_templates import templates as test
from data_templates.income_templates import templates as income
import os

test_config = {
    "output_path": 'output',
    'empty_path': 'empty.xls',
    'json_path': os.path.join('data_templates', 'income_json')
}

income_config = {
    "output_path": 'output',
    'empty_path': 'empty.xls',
    'json_path': os.path.join('data_templates', 'income_json')
}

TEMPLATE_DISPATCHER = {
    'Statistic': test,
    'IncomeSta': income
}

CONFIG_DISPATCHER = {
    'Statistic': test_config,
    'IncomeSta': income_config
}
