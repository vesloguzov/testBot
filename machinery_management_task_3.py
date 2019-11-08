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

# turning - Токарная
# drilling - Сверлильная
# milling - Фрезерная
# grinding - Шлифовальная

operations = [
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
]

operations = [
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
]

# operations = [
#     {
#         "id": "operation_1",
#         "title": u"опер1",
#         "duration": 1,
#     },
#     {
#         "id": "operation_2",
#         "title": u"опер2",
#         "duration": 0.9,
#     },
#     {
#         "id": "operation_3",
#         "title": u"опер3",
#         "duration": 1.1,
#     },
#     {
#         "id": "operation_4",
#         "title": u"опер4",
#         "duration": 2.1,
#     }
# ]


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

# print(employees)

month = 21  # рабочих дней
work_day = 2  # количество смен
work_shift = 8  # количество часов в смене
half_shift = 0.5  # пол смены
defect_percent = 16  # процентов
N_out = 12600  #  16799.98966 # количество выпуск. деталей (N выпуска)
# N_out = 23530


tact = (month * work_day * work_shift * 60) / N_out  # такт мин/шт
safety_stock = 5
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
        # print("-----------------------", workplace_item)


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

# период неизменной работы - ПНР

# 0 45 165 240
periods_vals = sorted(periods_vals)
periods = []
# print(periods_vals)
for i, p in enumerate(periods_vals):
    if i > 0:
        periods.append(p - sorted(periods_vals)[i - 1])

# print(periods)

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
                op_count_0 = len([o for o in current_workplaces_0 if get_overlap([periods_vals[p_index-1], period], [o["op_start"], o["op_end"]])])
                pair[operations[idx - 1]['id']]["KPPM"].append(op_count_0)
                op_count_1 = len([o for o in current_workplaces_1 if get_overlap([periods_vals[p_index-1], period], [o["op_start"], o["op_end"]])])
                pair[operation['id']]["KPPM"].append(op_count_1)
                out_0 = periods[p_index-1] / operations[idx-1]["duration"] * op_count_0  # round(,3)
                out_1 = periods[p_index-1] / operation["duration"] * op_count_1  # round(,3)

                pair[operations[idx - 1]['id']]["out"].append(out_0)
                pair[operation['id']]["out"].append(out_1)
                new_item['change'].append(round(out_0-out_1, 3))  # round(,3)

                # этот момент возможно неверный
                if p_index == 1:
                    new_item['zero_dynamic'].append(round(0 + new_item['change'][p_index-1], 3))
                else:
                    new_item['zero_dynamic'].append(round(new_item['zero_dynamic'][-1] + new_item['change'][p_index - 1], 3))

        new_item["pair"] = pair
        operations_pairs.append(new_item)

        min_dynamic_value = min(new_item["zero_dynamic"])
        dynamic_value = 0
        if 0 >= min_dynamic_value:
            dynamic_value = math.ceil(abs(min_dynamic_value))
        dynamic_value = safety_stock + dynamic_value
        new_item["dynamic_value"] = dynamic_value

# for y in operations:
#     print(y)

# print("----------------------------------------------------")

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
print(student_data)

def check_answer(exp, ans):
    student_answer = json.loads(ans)["answer"]
    pass



