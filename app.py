from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)
app.debug = True



class Output:

    @classmethod
    def clean(cls):
        import os
        filepath = 'output'
        files = os.listdir(filepath)
        for f in files:
            os.remove(os.path.join(filepath, f))

    @classmethod
    def output_income_excel(cls, duration):
        from statistics.income_sta import IncomeSta
        from statistics.routes.income_routes.routes import ROUTES_MAPPING

        for sheet in ROUTES_MAPPING.keys():
            print("正导出sheet: ", end='')
            print(sheet)
            income = IncomeSta(sheet, duration)
            income.output_sheet()
        print('营收报表导出成功')

    @classmethod
    def output_expend_excel(cls, gus_type, duration):
        from statistics.expend_sta import ExpendSta

        signs = [
            'sheet1_table1?gus_type',
            'sheet2_table1?gus_type',
            'sheet3_table1?gus_type',
            'sheet4_table1?car',
            'sheet5_table1?car',
            'sheet6_table1?car',
            'sheet7_table1',
            'sheet8_table1',
            'sheet9_table1',
            'sheet10_table1?car',
            'sheet11_table1',
            'sheet12_table1',
            'sheet13_table1',
            'sheet14_table1',
        ]

        from models.expend import Expend
        car_dict = {}
        cars = []
        for e in Expend.find_all():
            car_name = getattr(e, 'car')
            car_dict[car_name] = 1
        for c in car_dict.keys():
            cars.append(c)

        for s in signs:
            splited = s.split('?')
            sheet_name = splited[0]
            if len(splited) == 2:
                arg = splited[1]

                if arg == 'gus_type':
                    # 如果arg == gus_type, 传入gus_type 导入
                    signature = sheet_name + '?gus_type=' + gus_type
                    ExpendSta(signature, duration).output_sheet()
                elif arg == 'car':
                    # 如果arg == car, 找到所有车牌号, 导出所有车牌的记录
                    for c in cars:
                        signature = sheet_name + '?car=' + c
                        ExpendSta(signature, duration).output_sheet()
            else:
                ExpendSta(sheet_name, duration).output_sheet()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/loader')
def loader():
    from xls_loader.loader import load_expend_xls
    from xls_loader.loader import load_income_xls
    try:
        # 导入数据

        load_expend_xls()
        load_income_xls()
        return render_template('info.html', info='数据导入完成')
    except:
        return render_template('info.html', info='数据有问题, 检查文件')


@app.route('/output_all_show', methods=['GET'])
def output_all_show():
    return render_template('output_all_show.html')


@app.route('/output_show', methods=['GET'])
def output_show():
    # todo
    return 'ahha'


@app.route('/output', methods=['POST'])
def output():
    # todo
    return 'haha'


@app.route('/output_all', methods=['post'])
def output_all():
    form = request.form
    duration = [form.get('start_date'), form.get('end_date')]
    Output.clean()
    gus_type = form.get('gus_type')
    Output.output_income_excel(duration)
    Output.output_expend_excel(gus_type, duration)
    return render_template('info.html', info="导出成功")


@app.route('/info')
def info():
    return render_template('info.html', info='info')


if __name__ == '__main__':
    app.run()
