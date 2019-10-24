import json
import math

badge_height = 40

correct_radius = badge_height/2

# badge_08 - телефон
# badge_07 - запасный выход

correct_answer = '[{"class":"badge_01","center_y":372,"center_x":136,"current_x":96,"current_y":352},{"class":"badge_01","center_y":479,"center_x":47,"current_x":7,"current_y":459},{"class":"badge_01","center_y":213,"center_x":236,"current_x":196,"current_y":193},{"class":"badge_05","center_y":345,"center_x":578,"current_x":538,"current_y":325},{"class":"badge_05","center_y":304,"center_x":750,"current_x":710,"current_y":284},{"class":"badge_05","center_y":192,"center_x":751,"current_x":711,"current_y":172},{"class":"badge_08","center_y":458,"center_x":422,"current_x":382,"current_y":438},{"class":"badge_08","center_y":60,"center_x":421,"current_x":381,"current_y":40},{"class":"badge_09","center_y":105,"center_x":481,"current_x":461,"current_y":85},{"class":"badge_09","center_y":415,"center_x":516,"current_x":496,"current_y":395},{"class":"badge_10","center_y":250,"center_x":299,"current_x":279,"current_y":230},{"class":"badge_10","center_y":312,"center_x":516,"current_x":496,"current_y":292},{"class":"badge_11","center_y":105,"center_x":605,"current_x":585,"current_y":85},{"class":"badge_11","center_y":415,"center_x":299,"current_x":279,"current_y":395},{"class":"badge_12","center_y":327,"center_x":299,"current_x":279,"current_y":307},{"class":"badge_12","center_y":191,"center_x":515,"current_x":495,"current_y":171},{"class":"badge_14","center_y":417,"center_x":583,"current_x":563,"current_y":397},{"class":"badge_15","center_y":325,"center_x":255,"current_x":235,"current_y":305},{"class":"badge_16","center_y":465,"center_x":138,"current_x":118,"current_y":445},{"class":"badge_16","center_y":243,"center_x":623,"current_x":603,"current_y":223},{"class":"badge_16","center_y":259,"center_x":413,"current_x":393,"current_y":239},{"class":"badge_16","center_y":201,"center_x":142,"current_x":122,"current_y":181},{"class":"badge_17","center_y":107,"center_x":775,"current_x":755,"current_y":87},{"class":"badge_17","center_y":107,"center_x":299,"current_x":279,"current_y":87},{"class":"badge_17","center_y":373,"center_x":30,"current_x":10,"current_y":353}]'
correct_answer = json.loads(correct_answer)



def point_in_circle(c_r, c_x, c_y, p_x, p_y):
    result = False
    if math.pow((c_x - p_x), 2) + math.pow((c_y - p_y), 2) <= math.pow(c_r, 2):
        result = True
    return result


def check_answer(exp, ans):
    student_answer = json.loads(ans)  # ["answer"]
    max_grade = 0
    grade = 0

    incorrect_badges = []
    excess_badges = ["badge_14", "badge_15", "badge_16", "badge_17", "badge_18"]

    for badge in correct_answer:
        if not badge["class"] in excess_badges:
            max_grade = max_grade+1
            student_filtered_badges = list(filter(lambda x: x["class"] == badge["class"], student_answer))
            for filter_b in student_filtered_badges:
                if point_in_circle(
                        correct_radius,
                        badge["center_x"],
                        badge["center_y"],
                        filter_b["center_x"],
                        filter_b["center_y"]
                ):
                    grade = grade + 1
                    break
    
    result_grade = grade / max_grade
    msg = ""
    if result_grade == 1:
        return {'input_list': [{'ok': True, 'msg': msg, 'grade_decimal': 1}]}
    elif result_grade == 0:
        return {'input_list': [{'ok': False, 'msg': msg, 'grade_decimal': 0}]}
    else:
        return {'input_list': [{'ok': 'Partial', 'msg': msg, 'grade_decimal': result_grade}]}

    # print("Оценка: ", grade, " из ", max_grade)


st_answer = '[{"class":"badge_00","center_y":480,"center_x":49.5,"current_x":12,"current_y":460},{"class":"badge_00","center_y":210,"center_x":236.5,"current_x":199,"current_y":190},{"class":"badge_00","center_y":386,"center_x":135.5,"current_x":98,"current_y":366},{"class":"badge_04","center_y":304,"center_x":747.5,"current_x":710,"current_y":284},{"class":"badge_04","center_y":195,"center_x":746.5,"current_x":709,"current_y":175},{"class":"badge_04","center_y":347,"center_x":576.5,"current_x":539,"current_y":327},{"class":"badge_07","center_y":65,"center_x":422.5,"current_x":385,"current_y":45},{"class":"badge_07","center_y":467,"center_x":420.5,"current_x":383,"current_y":447},{"class":"badge_08","center_y":107,"center_x":476,"current_x":456,"current_y":87},{"class":"badge_08","center_y":339,"center_x":300,"current_x":280,"current_y":319},{"class":"badge_09","center_y":193,"center_x":514,"current_x":494,"current_y":173},{"class":"badge_10","center_y":103,"center_x":606,"current_x":586,"current_y":83},{"class":"badge_10","center_y":415,"center_x":296,"current_x":276,"current_y":395},{"class":"badge_11","center_y":416,"center_x":515,"current_x":495,"current_y":396},{"class":"badge_11","center_y":253,"center_x":301,"current_x":281,"current_y":233}]'

check_answer("", st_answer)

