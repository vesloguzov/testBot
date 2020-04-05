## -*- coding: utf-8 -*-
import json


def comparison_numbers(correct_number, student_number, tol=0.005):
    if type(student_number) == str:
        student_number = student_number.replace(",", ".")
    try:
        st_num = float(student_number)
        return tol >= abs(st_num - correct_number)
    except ValueError:
        return False


def check_triangles(expect, answer_given):
    student_answer = json.loads(answer_given)["answer"]
    side_1 = student_answer["side_1"]
    side_2 = student_answer["side_2"]
    side_3 = student_answer["side_3"]
    h_1 = student_answer["h_1"]
    h_2 = student_answer["h_2"]
    h_3 = student_answer["h_3"]

    s_1 = student_answer["S_1"]
    s_2 = student_answer["S_2"]
    s_3 = student_answer["S_3"]
    s_avg = student_answer["S_avg"]
    s_err = student_answer["S_err"]

    correct_s_1 = side_1 * h_1 * 0.5
    correct_s_2 = side_2 * h_2 * 0.5
    correct_s_3 = side_3 * h_3 * 0.5
    correct_s_avg = (correct_s_1 + correct_s_2 + correct_s_3) / 3

    correct_s_err = (abs(correct_s_avg-correct_s_1) + abs(correct_s_avg-correct_s_2) + abs(correct_s_avg-correct_s_3))/3

    print correct_s_1
    print correct_s_2
    print correct_s_3
    print correct_s_err

    grade = 0
    max_grade = 5

    response = {"S_1": False, "S_2": False, "S_3": False, "S_avg": False, "S_err": False, "comment": ""}

    if s_1 > 0 and comparison_numbers(correct_s_1, s_1):
        grade += 1
        response["S_1"] = True

    if s_2 > 0 and comparison_numbers(correct_s_2, s_2):
        grade += 1
        response["S_2"] = True

    if s_3 > 0 and comparison_numbers(correct_s_3, s_3):
        grade += 1
        response["S_3"] = True

    if s_1 > 0 and s_2 > 0 and s_3 > 0 and s_avg > 0 and comparison_numbers(correct_s_avg, s_avg):
        grade += 1
        response["S_avg"] = True

    if s_1 > 0 and s_2 > 0 and s_3 > 0 and s_avg > 0 and comparison_numbers(correct_s_err, s_err):
        grade += 1
        response["S_err"] = True

    if s_1 == 0 or s_2 == 0 or s_3 == 0 or s_avg == 0:
        response = {"S_1": False, "S_2": False, "S_3": False, "S_avg": False, "S_err": False, "comment": ""}
        response["comment"] = "Площадь треугольника не может быть равна нулю!"
        grade = 0

    if side_3 > side_1 + side_2 or side_2 > side_1 + side_3 or side_1 > side_2 + side_3:
        response = {"S_1": False, "S_2": False, "S_3": False, "S_avg": False, "S_err": False, "comment": ""}
        response["comment"] = "Измерения треугольника проведены не верно! Проверьте ход Ваших действий."
        grade = 0

    if abs((s_2 - s_1)) > s_2 * 0.25 or abs((s_2 - s_3)) > s_2 * 0.25:
        response = {"S_1": False, "S_2": False, "S_3": False, "S_avg": False, "S_err": False, "comment": ""}
        response["comment"] = "Площади треугольников посчитаны не верно! Проверьте ход Ваших действий."
        grade = 0

    result_grade = grade / float(max_grade)

    msg = json.dumps(response)
    if result_grade == 1:
        return {'input_list': [{'ok': True, 'msg': msg, 'grade_decimal': 1}]}
    elif result_grade == 0:
        return {'input_list': [{'ok': False, 'msg': msg, 'grade_decimal': 0}]}
    else:
        return {'input_list': [{'ok': 'Partial', 'msg': msg, 'grade_decimal': result_grade}]}

lol_answer = '{"answer":{"side_1":2,"h_1":3,"S_1":3,"side_2":4,"h_2":4,"S_2":8,"side_3":2,"h_3":2,"S_3":2,"S_avg":4.333333, "S_err":2.444}}'
print check_triangles(None, lol_answer)

