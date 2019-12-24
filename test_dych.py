# -*- coding: utf-8 -*-

from datetime import datetime

year_transition = {
    "transition_enable": True,
    "date": {
        "month": 7,
        "day": 1
    },
    "before": 775,
    "after": 776,
}


def check_years(expect, answer_given):
    birthday_str = answer_given[0].replace(" ", "")
    new_birthday_str = answer_given[1].replace(" ", "")

    msg_1 = ""
    msg_2 = ""

    grade = 0

    max_year = datetime.now().year - 10
    min_year = max_year - 200

    birthday = birthday_str.split(".")

    if len(birthday) == 3:
        try:
            day = int(birthday[0])
            month = int(birthday[1])
            year = int(birthday[2])

            if 31 >= day >= 1 and 12 >= month >= 1 and max_year >= year >= min_year:
                try:
                    new_birth = int(new_birthday_str)

                    if year_transition["transition_enable"]:
                        if month > year_transition["date"]["month"]:
                            new_birth_correct = year + year_transition["after"]
                        elif month == year_transition["date"]["month"]:
                            if day >= year_transition["date"]["day"]:
                                new_birth_correct = year + year_transition["after"]
                            else:
                                new_birth_correct = year + year_transition["before"]
                        else:
                            new_birth_correct = year + year_transition["before"]
                    else:
                        new_birth_correct = year + year_transition["before"]

                    # print("new_birth_correct:", new_birth_correct)
                    # print("new_birth:", new_birth)

                    if new_birth == new_birth_correct:
                        grade = 1
                        msg_2 = "Верный ответ!"
                    else:
                        msg_2 = "Неверный ответ!"

                except:
                    msg_2 = "Ошибка ввода года!"

            else:
                msg_1 = "Ошибка ввода даты рождения"

        except:
            msg_1 = "Ошибка ввода даты рождения"
    else:
        msg_1 = "Ошибка ввода даты рождения"

    if grade == 1:
        ok = True
    else:
        ok = False

    return_obj = {'input_list': [
                    {'ok': ok, 'msg': msg_1, 'grade_decimal': grade},
                    {'ok': ok, 'msg': msg_2, 'grade_decimal': grade}]}

    return return_obj


ans_1 = "4.1.1958"
ans_2 = "2733"

print(check_years(False, [ans_1, ans_2]))
