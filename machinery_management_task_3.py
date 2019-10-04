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
            if b.sum() + item['congestion'] <= max_size:
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


# turning - Токарная
# drilling - Сверлильная
# milling - Фрезерная
# grinding - Шлифовальная
pass
operations = [
    {
        "id": "operation_1",
        "title": "Токарная 1",
        "duration": 1.6,
        "type": "turning",
    },
    {
        "id": "operation_2",
        "title": "Токарная 2",
        "duration": 1.7,
        "type": "turning",
    },
    {
        "id": "operation_3",
        "title": "Сверлильная",
        "duration": 1.3,
        "type": "drilling",
    },
    {
        "id": "operation_4",
        "title": "Фрезерная",
        "duration": 3.2,
        "type": "milling",
    },
    {
        "id": "operation_5",
        "title": "Шлифовальная",
        "duration": 2.7,
        "type": "grinding",
    }
]

operations_weight = {
    "turning": {
        "weight": 0
    },
    "drilling": {
        "weight": 1
    },
    "milling": {
        "weight": 2
    },
    "grinding": {
        "weight": 3
    },
}

# operations = [
#     {
#         "id": "operation_1",
#         "title": "Токарная",
#         "duration": 1.9,
#         "type": "turning",
#     },
#     {
#         "id": "operation_2",
#         "title": "Сверлильная",
#         "duration": 1.1,
#         "type": "drilling",
#     },
#     {
#         "id": "operation_3",
#         "title": "Фрезерная",
#         "duration": 2.1,
#         "type": "milling",
#     },
#     {
#         "id": "operation_4",
#         "title": "Шлифовальная",
#         "duration": 1.3,
#         "type": "grinding",
#     }
# ]

employees = {
    "employee_1": {
        "id": "employee_1",
        "title": "Сашка",
    },
    "employee_2": {
        "id": "employee_2",
        "title": "Женьдос",
    },
    "employee_3": {
        "id": "employee_3",
        "title": "Славик",
    },
    "employee_4": {
        "id": "employee_4",
        "title": "Колян",
    },
    "employee_5": {
        "id": "employee_5",
        "title": "Лёха",
    },
    "employee_6": {
        "id": "employee_6",
        "title": "Паша",
    },
    "employee_7": {
        "id": "employee_7",
        "title": "Работник 1",
    },
    "employee_8": {
        "id": "employee_8",
        "title": "Работник 2",
    },
    "employee_9": {
        "id": "employee_9",
        "title": "Работник 3",
    },
    "employee_10": {
        "id": "employee_10",
        "title": "Работник 4",
    },
    "employee_11": {
        "id": "employee_11",
        "title": "Работник 5",
    },
    "employee_12": {
        "id": "employee_12",
        "title": "Работник 6",
    },
    "employee_13": {
        "id": "employee_13",
        "title": "Работник 7",
    },
    "employee_14": {
        "id": "employee_14",
        "title": "Работник 8",
    }
}

# print(employees)

month = 21  # рабочих дней
work_day = 2  # количество смен
work_shift = 8  # количество часов в смене
half_shift = 0.5  # пол смены
defect_percent = 16  # процентов
N_out =  16799.98966  #12600  # количество выпуск. деталей (N выпуска)
tact = (month * work_day * work_shift * 60) / N_out  # такт мин/шт
safety_stock = 5
#  N_in = N_out/(1-defect_percent*100)  # количество запуск. деталей (N запуска) это еще разобраться как считать

max_time = work_shift * half_shift * 60  # узнать как назвать переменную

workplaces = []

for op in operations:
    op_workplace_len = math.ceil(op["duration"] / tact)
    for workplace_num in list(range(0, op_workplace_len)):
        workplace_congestion = round(op["duration"] / tact, 4)

        if workplace_congestion - workplace_num > 1:
            workplace_congestion = 1
        else:
            workplace_congestion = workplace_congestion - workplace_num
        # workplace_item["weight"] =
        workplace_item = {
            "weight": operations_weight[op["type"]]["weight"],
            "type": op["type"],
            # "workplace_num": workplace_num,
            "congestion": round(workplace_congestion * 100, 2),  # загрузка рабочего места в процентах
            "work_time": round(workplace_congestion * max_time, 0)
        }
        workplaces.append(workplace_item)

workplaces_groups = first_fit(workplaces)

periods_vals = [0]

for idx, w in enumerate(workplaces_groups):
    current_employee = list(employees.keys())[idx]
    workplaces_groups[idx] = sorted(w, key=lambda i: i['weight'])
    for i, wp in enumerate(workplaces_groups[idx]):
        wp["employee"] = current_employee
        wp["employee_title"] = employees[current_employee]["title"]
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
periods = []
print(sorted(periods_vals))
for i, p in enumerate(sorted(periods_vals)):
    if i > 0: periods.append(p - sorted(periods_vals)[i - 1])


print(periods)


for index, l in enumerate(workplaces_groups):
    print("______________________________________")
    print("Рабочий", index + 1, " - ", l[0]['employee_title'])
    for g in l:
        print(g)

