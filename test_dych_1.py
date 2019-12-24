# -*- coding: utf-8 -*-
import json

trunks = {
    "tree": [1, 2, 11, 12, 21, 22, 31, 32, 41, 42, 51, 52],
    "fire": [3, 4, 13, 14, 23, 24, 33, 34, 43, 44, 53, 54],
    "land": [5, 6, 15, 16, 25, 27, 35, 37, 45, 47, 55, 57],
    "metal": [7, 8, 17, 18, 27, 28, 37, 38, 47, 48, 57, 58],
    "water": [9, 10, 19, 20, 29, 30, 39, 40, 49, 50, 59, 60]
}
branches = {
    "rat": [1, 13, 25, 37, 49],
    "bull": [2, 14, 26, 38, 50],
    "tiger": [3, 15, 27, 39, 51],
    "rabbit": [4, 16, 28, 40, 52],
    "dragon": [5, 17, 29, 41, 53],
    "snake": [6, 18, 30, 42, 54],
    "horse": [7, 19, 31, 43, 55],
    "sheep": [8, 20, 32, 44, 56],
    "monkey": [9, 21, 33, 45, 57],
    "cock": [10, 22, 34, 46, 58],
    "dog": [11, 23, 35, 47, 59],
    "pig": [12, 24, 36, 48, 60]
}


def check_answer(expect, answer_given):

    student_answer = json.loads(answer_given)
    student_trunk = student_answer["trunk"]
    student_branch = student_answer["branch"]

    result_grade = 0

    response = {
        "cell_num": {
            "correctness": False,
            "msg": ""
        },
         "trunk": {
            "correctness": False,
            "msg": ""
        },
         "branch": {
            "correctness": False,
            "msg": ""
        }
    }

    try:
        cell_num = int(student_answer["cell"])
        if 1 > cell_num or cell_num > 60:
            raise ValueError
    except:
        response["cell_num"]["msg"] = "Неверно введен номер клетки"
        return {'input_list': [{'ok': False, 'msg': json.dumps(response), 'grade_decimal': 0}]}

    if student_trunk in trunks.keys():
        if cell_num in trunks[student_trunk]:
            response["trunk"]["msg"] = "Небесный ствол выбран верно"
            result_grade += 0.5
        else:
            response["trunk"]["msg"] = "Небесный ствол выбран неверно"

    else:
        response["trunk"]["msg"] = "Не выбран небесный ствол"

    if student_branch in branches.keys():
        if cell_num in branches[student_branch]:
            response["branch"]["msg"] = "земная ветвь выбрана верно"
            result_grade += 0.5
        else:
            response["branch"]["msg"] = "земная ветвь выбрана неверно"
    else:
        response["branch"]["msg"] = "Не выбрана земная ветвь"

    if result_grade == 1:
        return {'input_list': [{'ok': True, 'msg': json.dumps(response), 'grade_decimal': 1}]}
    elif result_grade == 0:
        return {'input_list': [{'ok': False, 'msg': json.dumps(response), 'grade_decimal': 0}]}
    else:
        return {'input_list': [{'ok': 'Partial', 'msg': json.dumps(response), 'grade_decimal': result_grade}]}

student_answer_1 = '{"trunk":"tree","branch":"rat","cell":"01"}'
print(check_answer(False, student_answer_1))

