import json
import math

# operations = [
#     {
#         "id": "operation_1",
#         "title": "Токарная 1",
#         "duration": 1.6,
#         "type": "turning",
#     },
#     {
#         "id": "operation_2",
#         "title": "Токарная 2",
#         "duration": 1.7,
#         "type": "turning",
#     },
#     {
#         "id": "operation_3",
#         "title": "Сверлильная",
#         "duration": 1.3,
#         "type": "drilling",
#     },
#     {
#         "id": "operation_4",
#         "title": "Фрезерная",
#         "duration": 3.2,
#         "type": "milling",
#     },
#     {
#         "id": "operation_5",
#         "title": "Шлифовальная",
#         "duration": 2.7,
#         "type": "grinding",
#     }
# ]

operations = [
    {
        "id": "operation_1",
        "title": "Токарная",
        "duration": 1.9,
        "type": "turning",
    },
    {
        "id": "operation_2",
        "title": "Сверлильная",
        "duration": 1.1,
        "type": "drilling",
    },
    {
        "id": "operation_3",
        "title": "Фрезерная",
        "duration": 2.1,
        "type": "milling",
    },
    {
        "id": "operation_4",
        "title": "Шлифовальная",
        "duration": 1.3,
        "type": "grinding",
    }
]


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

print(employees)

month = 21  # рабочих дней
work_day = 2  # количество смен
work_shift = 8  # количество часов в смене
half_shift = 0.5  # пол смены
defect_percent = 16  # процентов
N_out = 12600  # количество выпуск. деталей (N выпуска)
tact = (month * work_day * work_shift * 60) / N_out  # такт мин/шт
#  N_in = N_out/(1-defect_percent*100)  # количество запуск. деталей (N запуска) это еще разобраться как считать

max_time = work_shift * half_shift * 60  # узнать как назвать переменную

workplaces = []

for op in operations:
    op_workplace_len = math.ceil(op["duration"] / tact)
    for workplace_num in list(range(0, op_workplace_len)):
        workplace_congestion = round(op["duration"]/tact, 4)

        if workplace_congestion - workplace_num > 1:
            workplace_congestion = 1
        else:
            workplace_congestion = workplace_congestion - workplace_num

        workplace_item = {
            "type": op["type"],
            "workplace_num": workplace_num,
            "congestion": workplace_congestion * 100,  # загрузка рабочего места в процентах
            "work_time": workplace_congestion * max_time
        }
        workplaces.append(workplace_item)


for w in workplaces:
    print(w)


# print(N_in)


print("Такт: ", tact)

# print(operations)
