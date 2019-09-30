import json

cities = ["city_0", "city_1", "city_2", "city_3", "city_4", "city_5", "city_6", "city_7", "city_8", "city_9",]

def check_answer(exp, ans):
    student_answer = json.loads(ans)["answer"]
    max_grade = len(cities)
    student_correct = []
    grade = 0
    for index, s_a in enumerate(student_answer):
        if s_a == cities[index]:
            grade += 1
            student_correct.append(s_a)
        else:
            grade = 0
            break
    result_grade = grade / max_grade
    msg = json.dumps(student_correct)
    if result_grade == 1:
        return {'input_list': [{'ok': True, 'msg': msg, 'grade_decimal': 1}]}
    elif result_grade == 0:
        return {'input_list': [{'ok': False, 'msg': msg, 'grade_decimal': 0}]}
    else:
        return {'input_list': [{'ok': 'Partial', 'msg': msg, 'grade_decimal': result_grade}]}



student_str = '{"answer":["city_0","city_1","city_2","city_3"]}'
print(check_answer(1, student_str))

