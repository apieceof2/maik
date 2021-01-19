from data_templates.income_templates import templates as test

test_config = {
    "output_path": 'output',
    'empty_path': 'empty.xls'
}

TEMPLATE_DISPATCHER = {
    'Statistic': test
}

CONFIG_DISPATCHER = {
    'Statistic': test_config
}
