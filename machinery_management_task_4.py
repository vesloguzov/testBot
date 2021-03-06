import json

subdivision_functions_count = 20
subdivision_count = 12

scheme = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, -1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, -1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, -1,-1,-1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, -1,-1,-1],
[1, 1, 1, 1, 1, 1, 0, -1,-1,-1,-1,-1],
[1, 1, 1, 1, 1, 1, 0, -1,-1,-1,-1,-1],
[1, 1, 1, 1, 1, 1, 0, -1,-1,-1,-1,-1],
[1, 1, 1, 1, 1, 1, 0, -1,-1,-1,-1,-1],
[1, 1, 1, 1, 1, 0, -1,-1,-1,-1,-1,-1],
[1, 1, 1, 1, 1, 0, -1,-1,-1,-1,-1,-1],
[1, 1, 1, 1, 1, 0, -1,-1,-1,-1,-1,-1],
[1, 1, 1, 1, 1, 0, -1,-1,-1,-1,-1,-1],
[1, 1, 1, 0, -1,-1,-1,-1,-1,-1,-1,-1],
[1, 1, 1, 0, -1,-1,-1,-1,-1,-1,-1,-1],
[1, 0, 0, 0, -1,-1,-1,-1,-1,-1,-1,-1],
[1, 0, 0, 0, -1,-1,-1,-1,-1,-1,-1,-1],
[0, 0, 0, -1,-1,-1,-1,-1,-1,-1,-1,-1],
[0, 0, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

# выше диагонали - 1
c = {
    "letter": "c",
    "name": u"c",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}
r = {
    "letter": "r",
    "name": u"r",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}

# ниже диагонали - 0
p = {
    "letter": "p",
    "name": u"p",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}
i = {
    "letter": "i",
    "name": u"i",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}

# без разницы где
u = {
    "letter": "u",
    "name": u"u",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}
s = {
    "letter": "s",
    "name": u"s",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}

# минимально требуемуе количество каждой буквы
min_every_letters_count = (subdivision_functions_count * subdivision_count) / 15

correct_percent_count_ranges = [
    {
        "start": 80,
        "end": 100,
        "coefficient": 1,
    },
    {
        "start": 60,
        "end": 80,
        "coefficient": 0.5,
    },
    # {
    #     "start": 0,
    #     "end": 60,
    #     "coefficient": 0.25,
    # },
    {
        "start": 0,
        "end": 60,
        "coefficient": 0,
    }
]

# print(min_every_letters_count)

in_every_row = [c, r, p, i]


def calculate_percent(obj, direction):
    """
     direction
        above
        below
    """

    direction_name = "above_diag" if direction == "above" else "below_diag"
    if obj["sum"] > 0:
        percent = round(obj[direction_name] / obj["sum"] * 100, 1)
    else:
        percent = 0
    # print("percent: ", percent)
    return percent


# def print_object(obj):
#     print("Буква:", obj["name"].upper(), "Всего букв в таблице: ", obj["sum"], "  |  ", calculate_percent(obj, "above"), "% выше диагонали,", calculate_percent(obj, "below"), "% ниже диагонали")


def get_coefficient(percent):
    if percent > 100:
        return 1
    for r in correct_percent_count_ranges:
        if percent >= r["start"] and r["end"] >= percent:
            return r["coefficient"]
    return 0


def check_answer(exp, ans):
    student_answer = json.loads(ans)["answer"]

    task_grade = 100

    max_grade_1 = subdivision_functions_count
    grade_1 = 0

    response = {"grade_1": {}, "grade_2": {"c": {}, "r": {}, "p": {}, "i": {}}}

    msg = ""

    for row_num in list(range(0, subdivision_functions_count)):

        student_row = [x.lower() for x in student_answer[row_num]]
        if all((item in student_row) for item in [l["name"] for l in in_every_row]):
            grade_1 = grade_1 + 1

        for letter_index, letter in enumerate(student_row):
            letter = letter.lower()
            if letter == c["name"]:
                c["sum"] = c["sum"] + 1
                if scheme[row_num][letter_index] > 0:
                    c["above_diag"] = c["above_diag"] + 1
                elif 0 > scheme[row_num][letter_index]:
                    c["below_diag"] = c["below_diag"] + 1
                else:

                    pass
            elif letter == r["name"]:
                r["sum"] = r["sum"] + 1
                if scheme[row_num][letter_index] > 0:
                    r["above_diag"] = r["above_diag"] + 1
                elif 0 > scheme[row_num][letter_index]:
                    r["below_diag"] = r["below_diag"] + 1
                else:

                    pass
            elif letter == p["name"]:
                p["sum"] = p["sum"] + 1
                if scheme[row_num][letter_index] > 0:
                    p["above_diag"] = p["above_diag"] + 1
                elif 0 > scheme[row_num][letter_index]:
                    p["below_diag"] = p["below_diag"] + 1
                else:

                    pass
            elif letter == i["name"]:
                i["sum"] = i["sum"] + 1
                if scheme[row_num][letter_index] > 0:
                    i["above_diag"] = i["above_diag"] + 1
                elif 0 > scheme[row_num][letter_index]:
                    i["below_diag"] = i["below_diag"] + 1
                else:

                    pass
            elif letter == u["name"]:
                u["sum"] = u["sum"] + 1
                if scheme[row_num][letter_index] > 0:
                    u["above_diag"] = u["above_diag"] + 1
                elif 0 > scheme[row_num][letter_index]:
                    u["below_diag"] = u["below_diag"] + 1
                else:

                    pass
            elif letter == s["name"]:
                s["sum"] = s["sum"] + 1
                if scheme[row_num][letter_index] > 0:
                    s["above_diag"] = s["above_diag"] + 1
                elif 0 > scheme[row_num][letter_index]:
                    s["below_diag"] = s["below_diag"] + 1
                else:

                    pass
            elif letter == "":
                # print("empty cell")
                pass
            else:
                pass

    max_grade_2 = len(in_every_row) * 5
    max_grade_2_criteria_1 = max_grade_2/2
    max_grade_2_criteria_2 = max_grade_2/2
    grade_2_base = max_grade_2 / len(in_every_row) / 2

    coeff_to_hundred = task_grade/(max_grade_2 + max_grade_1)

    grade_2 = 0

    msg += u'ЦРПИ в каждой строке: {} строк из {} верно'.format(grade_1, max_grade_1)

    for x in in_every_row:
        curr_grade = 0
        if x["sum"] > min_every_letters_count:
            curr_grade = max_grade_2_criteria_2 / len(in_every_row)
        response["grade_2"][x["letter"]]["criteria_2"] = str(curr_grade*coeff_to_hundred) + u' так как размещено букв ' + str(x["name"]).upper() + " " + str(x["sum"]) + u" штук при минимальном требовании " + str(min_every_letters_count)
        grade_2 += curr_grade
        response["grade_2"][x["letter"]]["criteria_2_grade"] = curr_grade*coeff_to_hundred
        # print("curr_grade: ", curr_grade)

    grade_2_c = grade_2_base * get_coefficient(calculate_percent(c, "above"))
    grade_2_r = grade_2_base * get_coefficient(calculate_percent(r, "above"))
    grade_2_p = grade_2_base * get_coefficient(calculate_percent(p, "below"))
    grade_2_i = grade_2_base * get_coefficient(calculate_percent(i, "below"))

    grade_2 += grade_2_c + grade_2_r + grade_2_p + grade_2_i

    # print("Оценка 1: ", grade_1, "/", max_grade_1)
    # print("Оценка 2: ", grade_2, "/", max_grade_2)

    result_max_grade = max_grade_1 + max_grade_2
    result_grade = (grade_1 + grade_2) / result_max_grade

    # print("Итоговая оценка: ", (grade_1 + grade_2), " из ", (max_grade_1 + max_grade_2), " ИЛИ", result_grade * 100, " из 100")

    response["max_grade"] = result_max_grade * coeff_to_hundred
    response["max_grade_1"] = max_grade_1 * coeff_to_hundred
    response["max_grade_2"] = max_grade_2 * coeff_to_hundred

    response["grade_1"] = u"За ЦРПИ в каждой строке набрано " + str(grade_1 * coeff_to_hundred) + u". Строк верно: " + str(grade_1) + u" из " + str(max_grade_1)
    response["grade_2"]["c"]["criteria_1"] = str(grade_2_c*coeff_to_hundred) + u" так как попало " + str(calculate_percent(c, "above")) + u"% всех размещенных букв примерно выше диагонали " + c["name"].upper()
    response["grade_2"]["c"]["criteria_1_grade"] = grade_2_c*coeff_to_hundred
    response["grade_2"]["r"]["criteria_1"] = str(grade_2_r*coeff_to_hundred) + u" так как попало " + str(calculate_percent(r, "above")) + u"% всех размещенных букв примерно выше диагонали " + r["name"].upper()
    response["grade_2"]["r"]["criteria_1_grade"] = grade_2_r*coeff_to_hundred
    response["grade_2"]["p"]["criteria_1"] = str(grade_2_p*coeff_to_hundred) + u" так как попало " + str(calculate_percent(p, "below")) + u"% всех размещенных букв примерно ниже диагонали " + p["name"].upper()
    response["grade_2"]["p"]["criteria_1_grade"] = grade_2_p*coeff_to_hundred
    response["grade_2"]["i"]["criteria_1"] = str(grade_2_i*coeff_to_hundred) + u" так как попало " + str(calculate_percent(i, "below")) + u"% всех размещенных букв примерно ниже диагонали " + i["name"].upper()
    response["grade_2"]["i"]["criteria_1_grade"] = grade_2_i*coeff_to_hundred

    if result_grade == 1:
        return {'input_list': [{'ok': True, 'msg': json.dumps(response), 'grade_decimal': 1}]}
    elif result_grade == 0:
        return {'input_list': [{'ok': False, 'msg': json.dumps(response), 'grade_decimal': 0}]}
    else:
        return {'input_list': [{'ok': 'Partial', 'msg': json.dumps(response), 'grade_decimal': result_grade}]}

    # print(response["grade_1"])
    # print(response["grade_2"]["c"])
    # print(response["grade_2"]["r"])
    # print(response["grade_2"]["p"])
    # print(response["grade_2"]["i"])
    #
    # print(response)

answer_str = '''
{
  "answer": 
[["с","р","п","И","у","с","с","у","с","с","п","у"],["р","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"]]
}
                '''

print(check_answer(False, answer_str))
