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

expend_config = {
    "output_path": 'output',
    'empty_path': 'empty.xls',
    'json_path': os.path.join('data_templates', 'expend_json')
}

CONFIG_DISPATCHER = {
    'Statistic': test_config,
    'IncomeSta': income_config,
    'ExpendSta': expend_config
}
