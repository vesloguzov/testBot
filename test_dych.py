import json

cities = [
    {
        "id": "city_0",
        "title": "Москва",
    },
    {
        "id": "city_10",
        "title": "Соликамск",
        "year": 1430,
    },
    {
        "id": "city_13",
        "title": "Тобольск",
        "year": 1587,
    },
    {
        "id": "city_12",
        "title": "Берёзово",
        "year": 1593,
    },
    {
        "id": "city_16",
        "title": "Сургут",
        "year": 1594,
    },
    {
        "id": "city_14",
        "title": "Обдорск (Салехард)",
        "year": 1595,
    },
    {
        "id": "city_19",
        "title": "Томск",
        "year": 1604,
    },
    {
        "id": "city_20",
        "title": "Красноярск",
        "year": 1628,
    },
    {
        "id": "city_21",
        "title": "Братск",
        "year": 1631,
    },
    {
        "id": "city_24",
        "title": "Якутск",
        "year": 1632,
    },
    {
        "id": "city_23",
        "title": "Чита",
        "year": 1653,
    },
    {
        "id": "city_32",
        "title": "Петропавловск-Камчатский",
        "year": 1740,
    },
    {
        "id": "city_28",
        "title": "Хабаровск",
        "year": 1858,
    },
    {
        "id": "city_30",
        "title": "Владивосток",
        "year": 1860,
    },
    {
        "id": "city_29",
        "title": "Анадырь",
        "year": 1889,
    }
]

correct_list = []

for index, x in enumerate(cities):
    if len(cities) > (index + 1):
        correct_list.append({"from": x["id"], "to": cities[index + 1]["id"]})

# print(correct_list)


def check_answer(exp, ans):
    student_answer = json.loads(ans)["answer"]
    max_grade = len(cities) - 1
    student_correct = {}

    for c_a in correct_list:
        s_a_id = next((l for l in student_answer.keys() if student_answer[l]['from'] == c_a["from"] and student_answer[l]['to'] == c_a["to"]), None)
        if s_a_id is not None:
            student_correct[s_a_id] = student_answer[s_a_id]
            student_correct[s_a_id]["to_year"] = next((l for l in cities if l['id'] == c_a["to"]), None)["year"]
            student_correct[s_a_id]["to_title"] = next((l for l in cities if l['id'] == c_a["to"]), None)["title"]
        else:
            break

    grade = len(student_correct.keys())
    result_grade = grade / max_grade
    msg = json.dumps(student_correct)
    if result_grade == 1:
        return {'input_list': [{'ok': True, 'msg': msg, 'grade_decimal': 1}]}
    elif result_grade == 0:
        return {'input_list': [{'ok': False, 'msg': msg, 'grade_decimal': 0}]}
    else:
        return {'input_list': [{'ok': 'Partial', 'msg': msg, 'grade_decimal': result_grade}]}


student_str = '{"answer":{"arrow_id_3ED3D8DC":{"from":"city_0","to":"city_10"},"arrow_id_DFCA4F5E":{"from":"city_10","to":"city_12"},"arrow_id_D94EA070":{"from":"city_12","to":"city_16"},"arrow_id_A3987041":{"from":"city_16","to":"city_18"},"arrow_id_2091DED3":{"from":"city_18","to":"city_19"},"arrow_id_93F25E21":{"from":"city_19","to":"city_20"},"arrow_id_413C07E4":{"from":"city_20","to":"city_21"}}}'
print(check_answer(1, student_str)['input_list'][0]['grade_decimal'])
# check_answer(1, student_str)
