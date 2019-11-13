import json
import math


def first_fit(list_items, max_size=100):
    class Bin:
        def __init__(self):
            self.list = []

        def addItem(self, item):
            self.list.append(item)

        def removeItem(self, item):
            self.list.remove(item)

        def sum(self):
            total = 0
            for elem in self.list:
                total += elem['congestion']
            return total

        def show(self):
            return self.list

    list_items = sorted(list_items, key=lambda i: i['congestion'], reverse=True)
    list_bins = [Bin()]

    for item in list_items:

        alloc_flag = False

        for b in list_bins:
            if max_size >= b.sum() + item['congestion']:
                b.addItem(item)
                alloc_flag = True
                break

        if not alloc_flag:
            new_bin = Bin()
            new_bin.addItem(item)
            list_bins.append(new_bin)

    list_items = []
    for b in list_bins:
        list_items.append(b.show())

    return list_items


def get_overlap(a, b):
    if max(0, min(a[1], b[1]) - max(a[0], b[0])) > 0:
        return True
    return False


employees = {
    "employee_1": {
        "id": "employee_1",
        "title": u"Сашка",
    },
    "employee_2": {
        "id": "employee_2",
        "title": u"Женьдос",
    },
    "employee_3": {
        "id": "employee_3",
        "title": u"Славик",
    },
    "employee_4": {
        "id": "employee_4",
        "title": u"Колян",
    },
    "employee_5": {
        "id": "employee_5",
        "title": u"Лёха",
    },
    "employee_6": {
        "id": "employee_6",
        "title": u"Паша",
    },
    "employee_7": {
        "id": "employee_7",
        "title": u"Работник 1",
    },
    "employee_8": {
        "id": "employee_8",
        "title": u"Работник 2",
    },
    "employee_9": {
        "id": "employee_9",
        "title": u"Работник 3",
    },
    "employee_10": {
        "id": "employee_10",
        "title": u"Работник 4",
    },
    "employee_11": {
        "id": "employee_11",
        "title": u"Работник 5",
    },
    "employee_12": {
        "id": "employee_12",
        "title": u"Работник 6",
    },
    "employee_13": {
        "id": "employee_13",
        "title": u"Работник 7",
    },
    "employee_14": {
        "id": "employee_14",
        "title": u"Работник 8",
    }
}

variants = [
    {
        "operations": [
            {
                "id": "operation_1",
                "title": u"Токарная 1",
                "duration": 1.6,
            },
            {
                "id": "operation_2",
                "title": u"Токарная 2",
                "duration": 1.7,
            },
            {
                "id": "operation_3",
                "title": u"Сверлильная",
                "duration": 1.3,
            },
            {
                "id": "operation_4",
                "title": u"Фрезерная",
                "duration": 3.2,
            },
            {
                "id": "operation_5",
                "title": u"Шлифовальная",
                "duration": 2.7,
            }
        ],
        "N_out": 16799.98966,
        "safety_stock": 5,
        "defect_percent": 16,
    },
    {
        "operations": [
            {
                "id": "operation_1",
                "title": u"Токарная",
                "duration": 1.9,
            },
            {
                "id": "operation_2",
                "title": u"Сверлильная",
                "duration": 1.1,
            },
            {
                "id": "operation_3",
                "title": u"Фрезерная",
                "duration": 2.1,
            },
            {
                "id": "operation_4",
                "title": u"Шлифовальная",
                "duration": 1.3,
            }
        ],
        "N_out": 12600,
        "safety_stock": 5,
        "defect_percent": 16,
    },
]

variant = variants[0]
operations = variant["operations"]

month = 21  # рабочих дней
work_day = 2  # количество смен
work_shift = 8  # количество часов в смене
half_shift = 0.5  # пол смены
defect_percent = variant["defect_percent"]
N_out = variant["N_out"]  # 16799.98966 # количество выпуск. деталей (N выпуска)
safety_stock = variant["safety_stock"]
# N_out = 23530

tact = (month * work_day * work_shift * 60) / N_out  # такт мин/шт

#  N_in = N_out/(1-defect_percent*100)  # количество запуск. деталей (N запуска) это еще разобраться как считать

max_time = work_shift * half_shift * 60  # узнать как назвать переменную

workplaces = []

for index, op in enumerate(operations):
    op["weight"] = index
    op_workplace_len = int(math.ceil(op["duration"] / tact))
    for workplace_num in list(range(0, op_workplace_len)):
        workplace_congestion = round(op["duration"] / tact, 4)

        if workplace_congestion - workplace_num > 1:
            workplace_congestion = 1
        else:
            workplace_congestion = workplace_congestion - workplace_num
        workplace_item = {
            "weight": op["weight"],
            "type": op["id"],
            "workplace_num": workplace_num,
            "congestion": round(workplace_congestion * 100, 2),
            "work_time": round(workplace_congestion * max_time, 1)
        }
        workplaces.append(workplace_item)

workplaces_groups = first_fit(workplaces)

periods_vals = [0]

for idx, w in enumerate(workplaces_groups):
    current_employee = list(employees.keys())[idx]
    workplaces_groups[idx] = sorted(w, key=lambda i: i['weight'])
    for i, wp in enumerate(workplaces_groups[idx]):
        wp["employee"] = current_employee
        # wp["employee_title"] = employees[current_employee]["title"]
        if i == 0:
            wp["op_start"] = 0
            wp["op_len"] = wp['work_time']
        else:
            wp["op_start"] = sum([l["work_time"] for l in workplaces_groups[idx]][0:i])
            wp["op_len"] = wp['work_time']
        wp["op_end"] = wp["op_start"] + wp["op_len"]
        if not wp["op_end"] in periods_vals:
            periods_vals.append(wp["op_end"])

periods_vals = sorted(periods_vals)
periods = []

for i, p in enumerate(periods_vals):
    if i > 0:
        periods.append(p - sorted(periods_vals)[i - 1])

workplaces = []
for index, l in enumerate(workplaces_groups):
    for g in l:
        workplaces.append(g)

operations_pairs = []
for idx, operation in enumerate(operations):
    if idx > 0:
        new_item = {}
        pair = {operations[idx - 1]['id']: {}, operation['id']: {}}

        pair[operations[idx - 1]['id']]["KPPM"] = []
        pair[operation['id']]["KPPM"] = []
        pair[operations[idx - 1]['id']]["out"] = []
        pair[operation['id']]["out"] = []
        new_item['change'] = []
        new_item['zero_dynamic'] = []

        current_workplaces_0 = [v for v in workplaces if (v["type"] == list(pair.keys())[0])]
        current_workplaces_1 = [v for v in workplaces if (v["type"] == list(pair.keys())[1])]

        for p_index, period in enumerate(periods_vals):
            if p_index > 0:
                op_count_0 = len([o for o in current_workplaces_0 if
                                  get_overlap([periods_vals[p_index - 1], period], [o["op_start"], o["op_end"]])])
                pair[operations[idx - 1]['id']]["KPPM"].append(op_count_0)
                op_count_1 = len([o for o in current_workplaces_1 if
                                  get_overlap([periods_vals[p_index - 1], period], [o["op_start"], o["op_end"]])])
                pair[operation['id']]["KPPM"].append(op_count_1)
                out_0 = periods[p_index - 1] / operations[idx - 1]["duration"] * op_count_0  # round(,3)
                out_1 = periods[p_index - 1] / operation["duration"] * op_count_1  # round(,3)

                pair[operations[idx - 1]['id']]["out"].append(out_0)
                pair[operation['id']]["out"].append(out_1)
                new_item['change'].append(round(out_0 - out_1, 3))  # round(,3)

                # этот момент возможно неверный
                if p_index == 1:
                    new_item['zero_dynamic'].append(round(0 + new_item['change'][p_index - 1], 3))
                else:
                    new_item['zero_dynamic'].append(
                        round(new_item['zero_dynamic'][-1] + new_item['change'][p_index - 1], 3))

        new_item["pair"] = pair
        operations_pairs.append(new_item)

        min_dynamic_value = min(new_item["zero_dynamic"])
        dynamic_value = 0
        if 0 >= min_dynamic_value:
            dynamic_value = math.ceil(abs(min_dynamic_value))
        dynamic_value = safety_stock + dynamic_value
        new_item["dynamic_value"] = dynamic_value

student_data = {
    "operations": operations,
    "employees": employees,
    "companion_data": {
        "month": month,
        "work_day": work_day,
        "work_shift": work_shift,
        "half_shift": half_shift,
        "defect_percent": defect_percent,
        "N_out": N_out,
        "safety_stock": safety_stock,
        "max_time": max_time,
    },
    "workplaces": [w["type"] for w in workplaces],
    "periods_len": len(periods),
    "operations_pairs": [list(y['pair'].keys()) for y in operations_pairs],
}


def workplaces_employees(tmp_workplaces):
    unique_employees = []
    for t_ind, t_wp in enumerate(tmp_workplaces):
        if t_wp["employee"] not in unique_employees:
            unique_employees.append(t_wp["employee"])
    res = []
    for unique_emp in unique_employees:
        res_sub = []
        for ind, w_emp in enumerate(tmp_workplaces):
            if w_emp["employee"] == unique_emp:
                res_sub.append(ind)
        res.append(res_sub)
    return sorted(res)


def comparison_numbers(correct_number, student_number, tol=0.05):
    if type(student_number) == str:
        student_number = student_number.replace(",", ".")
    try:
        st_num = float(student_number)
        return tol >= abs(st_num - correct_number)
    except ValueError:
        return False


def comparison_numbers_arrays(correct_array, student_array, tol=0.05):
    return all(comparison_arrays(correct_array, student_array, tol=0.05))


def comparison_arrays(correct_array, student_array, tol=0.05):

    if len(correct_array) != len(student_array):
        return [False for x in correct_array]
    else:
        ret_arr = []
        for idx, c_a in enumerate(correct_array):
            if comparison_numbers(c_a, student_array[idx], tol):
                ret_arr.append(True)
            else:
                ret_arr.append(False)
        return ret_arr


def check_answer(exp, ans):
    student_answer = json.loads(ans)["answer"]
    correct_workplaces = sorted(workplaces, key=lambda k: k['weight'])
    response = {
        "tact_value": False,
        "workplaces_table": False,
        "periods_table": False,
        "operations_pairs": []
    }

    tact_equal = comparison_numbers(tact, student_answer["tact"])
    response["tact_value"] = tact_equal

    work_time_equal = comparison_numbers_arrays([x["work_time"] for x in correct_workplaces], [x["work_time"] for x in student_answer["workplaces"]])
    employees_equal = workplaces_employees(correct_workplaces) == workplaces_employees(student_answer["workplaces"])
    operation_equal = [cw["type"] for cw in correct_workplaces] == [cw["type"] for cw in student_answer["workplaces"]]

    response["workplaces_table"] = work_time_equal and employees_equal and operation_equal

    response["periods_table"] = {
        "periods": comparison_arrays(periods, student_answer["periods"]),
        "result": comparison_numbers_arrays(periods, student_answer["periods"]),
    }

    for pair_index, op_corr in enumerate(operations_pairs):
        op_res = {
            "KPPM_1": comparison_arrays(op_corr["pair"][sorted(op_corr["pair"].keys())[0]]["KPPM"], student_answer["operations_pairs"][pair_index]["pair"][0]["KPPM"]),
            "KPPM_2": comparison_arrays(op_corr["pair"][sorted(op_corr["pair"].keys())[1]]["KPPM"], student_answer["operations_pairs"][pair_index]["pair"][1]["KPPM"]),
            "out_1":  comparison_arrays(op_corr["pair"][sorted(op_corr["pair"].keys())[0]]["out"], student_answer["operations_pairs"][pair_index]["pair"][0]["out"]),
            "out_2":  comparison_arrays(op_corr["pair"][sorted(op_corr["pair"].keys())[1]]["out"], student_answer["operations_pairs"][pair_index]["pair"][1]["out"]),
            "dynamic": comparison_numbers(op_corr["dynamic_value"], student_answer["operations_pairs"][pair_index]["dynamic_value"])
        }
        op_res["result"] = all(op_res["KPPM_1"]) and all(op_res["KPPM_2"]) and all(op_res["out_1"]) and all(op_res["out_2"]) and op_res["dynamic"]
        response["operations_pairs"].append(op_res)

    max_grade = 100
    grade = 0

    grade += 5 if response["tact_value"] else 0
    grade += 30 if response["workplaces_table"] else 0
    grade += 5 if response["periods_table"]["result"] else 0

    for op_grade in response["operations_pairs"]:
        if op_grade["result"]:
            grade += 60 / len(response["operations_pairs"])

    result_grade = grade / max_grade

    print("result_grade: ", result_grade)

    print(json.dumps(response))


st_answer = '{"answer":{"tact":0,"periods":[80,20,20,60,60],"workplaces":[{"type":"operation_1","congestion":100,"employee":"employee_7","work_time":240,"op_start":0,"op_end":240},{"type":"operation_1","congestion":33.33,"employee":"employee_5","work_time":80,"op_start":0,"op_end":80},{"type":"operation_2","congestion":100,"employee":"employee_8","work_time":240,"op_start":0,"op_end":240},{"type":"operation_2","congestion":41.67,"employee":"employee_6","work_time":100,"op_start":0,"op_end":100},{"type":"operation_3","congestion":100,"employee":"employee_9","work_time":240,"op_start":0,"op_end":240},{"type":"operation_3","congestion":8.33,"employee":"employee_6","work_time":20,"op_start":100,"op_end":120},{"type":"operation_4","congestion":100,"employee":"employee_10","work_time":240,"op_start":0,"op_end":240},{"type":"operation_4","congestion":100,"employee":"employee_11","work_time":240,"op_start":0,"op_end":240},{"type":"operation_4","congestion":66.67,"employee":"employee_5","work_time":160,"op_start":80,"op_end":240},{"type":"operation_5","congestion":100,"employee":"employee_12","work_time":240,"op_start":0,"op_end":240},{"type":"operation_5","congestion":100,"employee":"employee_13","work_time":240,"op_start":0,"op_end":240},{"type":"operation_5","congestion":25,"employee":"employee_6","work_time":60,"op_start":120,"op_end":180}],"operations_pairs":[{"dynamic_value":11,"changes":[5.882,-11.029,0.735,2.206,2.206],"dynamics":[16.882,5.853,6.588,8.794,11],"pair":[{"id":"operation_1","KPPM":[2,1,1,1,1],"out":[100,12.5,12.5,37.5,37.5]},{"id":"operation_2","KPPM":[2,2,1,1,1],"out":[94.1176,23.5294,11.7647,35.29411,35.29411]}]},{"dynamic_value":6,"changes":[32.579,8.145,-19.005,-10.86,-10.86],"dynamics":[38.579,46.724,27.719,16.859,5.999],"pair":[{"id":"operation_2","KPPM":[2,2,1,1,1],"out":[94.117647058823,23.5294117647,11.764705882,35.2941176,35.2941176]},{"id":"operation_3","KPPM":[1,1,2,1,1],"out":[61.538461,15.384615,30.76923,46.15384615,46.15384615]}]},{"dynamic_value":5,"changes":[11.538,15.385,12.019,-10.096,-10.096],"dynamics":[16.538,31.923,43.942,33.846,23.75],"pair":[{"id":"operation_3","KPPM":[1,1,2,1,1],"out":[61.538461538,15.384615384,30.76923,46.15384615,46.15384615]},{"id":"operation_4","KPPM":[2,3,3,3,3],"out":[50,0,18.75,56.25,56.25]}]},{"dynamic_value":17,"changes":[-9.259,3.935,3.935,-10.417,11.806],"dynamics":[7.741,11.676,15.611,5.194,17],"pair":[{"id":"operation_4","KPPM":[2,3,3,3,3],"out":[50,18.75,18.75,56.25,56.25]},{"id":"operation_5","KPPM":[2,2,2,3,2],"out":[59.2592592,14.81481481,14.81481481,66.666666,44.44444]}]}]}}'

check_answer(False, st_answer)