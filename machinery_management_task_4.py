import json

subdivision_functions_count = 20
subdivision_count = 12

scheme = [[1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 0, -1, -1, -1],
          [1, 1, 1, 1, 1, 1, 1, 1, 0, -1, -1, -1],
          [1, 1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1],
          [1, 1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1],
          [1, 1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1],
          [1, 1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1],
          [1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1, -1],
          [1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1, -1],
          [1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1, -1],
          [1, 1, 1, 1, 1, 0, -1, -1, -1, -1, -1, -1],
          [1, 1, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1],
          [1, 1, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1],
          [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],
          [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],
          [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1],
          [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1]]

# выше диагонали - 1
c = {
    "letter": "c",
    "name": "ц",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}
r = {
    "letter": "r",
    "name": "р",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}

# ниже диагонали - 0
p = {
    "letter": "p",
    "name": "п",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}
i = {
    "letter": "i",
    "name": "и",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}

# без разницы где
u = {
    "letter": "u",
    "name": "у",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}
s = {
    "letter": "s",
    "name": "с",
    "above_diag": 0,
    "below_diag": 0,
    "sum": 0,
}

min_every_letters_count = (subdivision_functions_count * subdivision_count) / 10

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
    #     "start": 40,
    #     "end": 60,
    #     "coefficient": 0.25,
    # },

    {
        "start": 0,
        "end": 60,
        "coefficient": 0,
    }
]

print(min_every_letters_count)

in_every_row = [c, r, p, i]


def calculate_percent(obj, direction):
    """
     direction
        above
        below
    """

    direction_name = "above_diag" if direction == "above" else "below_diag"
    percent = round(obj[direction_name] / obj["sum"] * 100, 1)
    # print("percent: ", percent)
    return percent


def print_object(obj):
    print("Буква:", obj["name"].upper(), "Всего букв в таблице: ", obj["sum"], "  |  ", calculate_percent(obj, "above"),
          "% выше диагонали,", calculate_percent(obj, "below"), "% ниже диагонали")


def get_coefficient(percent):
    for range in correct_percent_count_ranges:
        if range["start"] <= percent and range["end"] >= percent:
            return range["coefficient"]
    return 0


def check_answer(exp, ans):
    student_answer = json.loads(ans)["answer"]

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
                elif scheme[row_num][letter_index] < 0:
                    c["below_diag"] = c["below_diag"] + 1
                else:

                    pass
            elif letter == r["name"]:
                r["sum"] = r["sum"] + 1
                if scheme[row_num][letter_index] > 0:
                    r["above_diag"] = r["above_diag"] + 1
                elif scheme[row_num][letter_index] < 0:
                    r["below_diag"] = r["below_diag"] + 1
                else:

                    pass
            elif letter == p["name"]:
                p["sum"] = p["sum"] + 1
                if scheme[row_num][letter_index] > 0:
                    p["above_diag"] = p["above_diag"] + 1
                elif scheme[row_num][letter_index] < 0:
                    p["below_diag"] = p["below_diag"] + 1
                else:

                    pass
            elif letter == i["name"]:
                i["sum"] = i["sum"] + 1
                if scheme[row_num][letter_index] > 0:
                    i["above_diag"] = i["above_diag"] + 1
                elif scheme[row_num][letter_index] < 0:
                    i["below_diag"] = i["below_diag"] + 1
                else:

                    pass
            elif letter == u["name"]:
                u["sum"] = u["sum"] + 1
                if scheme[row_num][letter_index] > 0:
                    u["above_diag"] = u["above_diag"] + 1
                elif scheme[row_num][letter_index] < 0:
                    u["below_diag"] = u["below_diag"] + 1
                else:

                    pass
            elif letter == s["name"]:
                s["sum"] = s["sum"] + 1
                if scheme[row_num][letter_index] > 0:
                    s["above_diag"] = s["above_diag"] + 1
                elif scheme[row_num][letter_index] < 0:
                    s["below_diag"] = s["below_diag"] + 1
                else:

                    pass
            elif letter == "":
                # print("empty cell")
                pass
            else:
                pass

    max_grade_2 = len(in_every_row) * 5
    grade_2_base = max_grade_2 / len(in_every_row) / 2
    print("grade_2_base: ", grade_2_base)
    grade_2 = 0

    msg += 'ЦРПИ в каждой строке: {} строк из {} верно'.format(grade_1, max_grade_1)

    for x in in_every_row:

        # msg += '\nБукв {} содержится {} при минимальном количестве {} '.format(x["name"].upper(), x["sum"], min_every_letters_count)

        curr_grade = 0

        if x["sum"] > min_every_letters_count:
            curr_grade = max_grade_2 / len(in_every_row) / 2

        response["grade_2"][x["letter"]]["criteria_2"] = str((curr_grade/max_grade_2)*100) + ' так как размещено букв ' + str(x["name"]).upper() + " " + str(x["sum"]) + " штук при минимальном требовании " + str(min_every_letters_count)
            # msg += "Правильно"

        grade_2 += curr_grade

        # else:
            # msg += "Неправильно"

    grade_2_c = grade_2_base * get_coefficient(calculate_percent(c, "above"))
    grade_2_r = grade_2_base * get_coefficient(calculate_percent(r, "above"))
    grade_2_p = grade_2_base * get_coefficient(calculate_percent(p, "below"))
    grade_2_i = grade_2_base * get_coefficient(calculate_percent(i, "below"))

    grade_2 += grade_2_c + grade_2_r + grade_2_p + grade_2_i

    print("Оценка 1: ", grade_1, "/", max_grade_1)
    print("Оценка 2: ", grade_2, "/", max_grade_2)

    result_max_grade = max_grade_1 + max_grade_2
    result_grade = (grade_1 + grade_2) / result_max_grade



    print("Итоговая оценка: ", (grade_1 + grade_2), " из ", (max_grade_1 + max_grade_2), " ИЛИ", result_grade * 100," из 100")

    response["grade_1"] = "За ЦРПИ в каждой строке набрано " + str((grade_1 / result_max_grade) * 100) + ". Строк верно: " + str(grade_1) + " из " + str(max_grade_1)

    # print(max_grade_2)

    response["grade_2"]["c"]["criteria_1"] = str((grade_2_c/max_grade_2)*100) + " так как попало " + str(calculate_percent(c, "above")) + "% всех размещенных букв примерно выше диагонали" + c["name"].upper()
    response["grade_2"]["r"]["criteria_1"] = str((grade_2_r/max_grade_2)*100) + " так как попало " + str(calculate_percent(r, "above")) + "% всех размещенных букв примерно выше диагонали" + r["name"].upper()
    response["grade_2"]["p"]["criteria_1"] = str((grade_2_p/max_grade_2)*100) + " так как попало " + str(calculate_percent(p, "below")) + "% всех размещенных букв примерно ниже диагонали" + p["name"].upper()
    response["grade_2"]["i"]["criteria_1"] = str((grade_2_i/max_grade_2)*100) + " так как попало " + str(calculate_percent(i, "below")) + "% всех размещенных букв примерно ниже диагонали" + i["name"].upper()

    print(response["grade_1"])
    print(response["grade_2"]["c"])
    print(response["grade_2"]["r"])
    print(response["grade_2"]["p"])
    print(response["grade_2"]["i"])

    # print(msg)

    # print(msg)


answer_str = '''
{
  "answer": 
[["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"],["ц","р","п","И","у","с","с","у","с","с","п","у"]]
}
                '''

check_answer(False, answer_str)
