import json

types = ["machine", "aggregate", "node", "detail"]

structure = {
    "type": "machine",
    "id": "machine_1",
    "duration": 6,
    "title": u"Машина",
    "children": [
        {
            "type": "aggregate",
            "id": "aggregate_1",
            "duration": 4,
            "title": u"Аггрегат",
            "children": [
                {
                    "type": "node",
                    "id": "node_1",
                    "duration": 4,
                    "title": u"Узел 1",
                    "children": [
                        {
                            "type": "detail",
                            "id": "detail_1_1",
                            "duration": 3,
                            "title": u"Деталь 1.1"
                        },
                        {
                            "type": "detail",
                            "id": "detail_1_2",
                            "duration": 2,
                            "title": u"Деталь 1.2"
                        },
                        {
                            "type": "detail",
                            "id": "detail_1_3",
                            "duration": 4,
                            "title": u"Деталь 1.3"
                        }
                    ]
                },
                {
                    "type": "node",
                    "id": "node_2",
                    "duration": 5,
                    "title": u"Узел 2",
                    "children": [
                        {
                            "type": "detail",
                            "id": "detail_2_1",
                            "duration": 4,
                            "title": u"Деталь 2.1"
                        },
                        {
                            "type": "detail",
                            "id": "detail_2_2",
                            "duration": 3,
                            "title": u"Деталь 2.2"
                        },
                        {
                            "type": "detail",
                            "id": "detail_2_3",
                            "duration": 3,
                            "title": u"Деталь 2.3"
                        }
                    ]
                },
            ]
        },
        {
            "type": "node",
            "id": "node_3",
            "duration": 6,
            "title": u"Узел 3",
            "children": [
                {
                    "type": "detail",
                    "id": "detail_3_1",
                    "duration": 2,
                    "title": u"Деталь 3.1"
                },
                {
                    "type": "detail",
                    "id": "detail_3_2",
                    "duration": 1,
                    "title": u"Деталь 3.2"
                },
                {
                    "type": "detail",
                    "id": "detail_3_3",
                    "duration": 4,
                    "title": u"Деталь 3.3"
                }
            ]
        },
        {
            "type": "node",
            "id": "node_4",
            "duration": 3,
            "title": u"Узел 4",
            "children": [
                {
                    "type": "detail",
                    "id": "detail_4_1",
                    "duration": 3,
                    "title": u"Деталь 4.1"
                },
                {
                    "type": "detail",
                    "id": "detail_4_2",
                    "duration": 2,
                    "title": u"Деталь 4.2"
                },
                {
                    "type": "detail",
                    "id": "detail_4_3",
                    "duration": 3,
                    "title": u"Деталь 4.3"
                }
            ]
        },
        {
            "type": "detail",
            "id": "detail_5",
            "duration": 3,
            "title": u"Деталь 5"
        },
        {
            "type": "detail",
            "id": "detail_6",
            "duration": 3,
            "title": u"Деталь 6"
        }
    ]
}


def get_list_from_structure(struct):
    s_list = []

    def get_elem(elem, current_d):
        tmp_obj = {
            "type": elem["type"],
            "id": elem["id"],
            "duration": elem["duration"],
            "title": elem["title"],
            "end_on": elem["duration"] + current_d
        }
        s_list.append(tmp_obj)
        if "children" in elem.keys():
            for x in elem['children']:
                get_elem(x, tmp_obj["end_on"])
    get_elem(struct, 0)

    return s_list


source_list = get_list_from_structure(structure)
problem_elements = []
extra_cells_count = 7

details = [x for x in source_list if x['type'] == 'detail']
area_height = len(details)
area_width = max([x['end_on'] for x in details])

student_list = []
for r in source_list:
    student_list_item = r
    del student_list_item["end_on"]
    student_list.append(student_list_item)

student_data = {
    "data": student_list,
    "area_height": area_height,
    "area_width": area_width,
    "extra_cells_count": extra_cells_count,
}

print(student_data["data"])
# print(student_data["area_width"])
# print(student_data["extra_cells_count"])

def get_details_count(elem):
    details_list = []
    details_list_count = 1
    def get_item(el):
        if "children" in el.keys():
            for x in el['children']:
                if x["type"] == "detail":
                    details_list.append(x)
                else:
                    get_item(x)
    get_item(elem)

    if len(details_list) > 0:
        details_list_count = len(details_list)
    return details_list_count


def get_element_children(student_obj, element):
    ret_list = []
    # print(element)
    for k in student_obj.keys():
        if (student_obj[k]['x'] + student_obj[k]['width'] == element['x']) and (student_obj[k]['y'] >= element['y'] and element['y'] + element['height'] >= student_obj[k]['y'] + student_obj[k]['height']):
            ret_list.append(student_obj[k])
    # print("children: ", [x["id"] for x in ret_list])
    # print("_________________________________________________")
    return ret_list


def intersects(a, b):
    a_coords = {
        "x": a['x'],
        "y": area_height - a['y'],
        "x1": a['x'] + a['width'],
        "y1": area_height - a['y'] - a['height'],
    }
    b_coords = {
        "x": b['x'],
        "y": area_height - b['y'],
        "x1": b['x'] + b['width'],
        "y1": area_height - b['y'] - b['height'],
    }
    return not (b_coords['y1'] >= a_coords['y'] or a_coords['y1'] >= b_coords['y'] or b_coords['x'] >= a_coords['x1'] or a_coords['x'] >= b_coords['x1'])


def check_children_intersections(children_list):
    no_intersect = True
    for child in children_list:
        for child_1 in children_list:
            if child["id"] != child_1["id"]:
                if intersects(child, child_1):
                    print("Нашли пересечение: ", child["id"])
                    problem_elements.append(child["id"])
                    no_intersect = False
    return no_intersect


def check_children_widths(student_obj, correct_children):
    correctness = True
    for child in correct_children:
        if child["duration"] != student_obj[child["id"]]["width"]:
            print("Нашли разные длины: ", child["id"])
            problem_elements.append(child["id"])
            correctness = False
    return correctness


def check_children_heights(student_obj, correct_children):
    correctness = True
    for child in correct_children:
        if get_details_count(child) != student_obj[child["id"]]["height"]:
            print("Нашли разные высоты: ", child["id"])
            problem_elements.append(child["id"])
            correctness = False
    return correctness


def check_children_equal(student_children, correct_children):
    if set(student_children) == set(correct_children):
        return True
    else:
        print("Нашли разных детей: ")
        for problem in list(set(student_children) - set(correct_children)) + list((set(correct_children) - set(student_children))):
            problem_elements.append(problem)
        return False

student_data_json = json.dumps(student_data, ensure_ascii=False).replace("\"", "'")

def check_answer(exp, ans):
    answer_obj = json.loads(ans)["answer"]
    user_machine = answer_obj[structure["id"]]
    grade = 0

    if user_machine['width'] == structure["duration"] and user_machine['x'] == area_width + extra_cells_count - structure["duration"] and user_machine['y'] == 0 and user_machine['height'] == area_height:
        def rec_check(student_el, cor_obj):
            if "children" in cor_obj.keys():
                children_ids_correct = [x["id"] for x in cor_obj['children']]
                children_ids_student = [x["id"] for x in get_element_children(answer_obj, student_el)]

                if check_children_equal(children_ids_student, children_ids_correct) and check_children_intersections([answer_obj[x] for x in children_ids_student]) and check_children_widths(answer_obj, cor_obj["children"]) and check_children_heights(answer_obj, cor_obj["children"]):
                    for c in cor_obj["children"]:
                        if c["type"] != "detail":
                            rec_check(answer_obj[c["id"]], c)
                        else:
                            pass
                else:
                    pass
        rec_check(user_machine, structure)
    else:
        problem_elements.append(structure["id"])

    if len(problem_elements) == 0:
        grade = 1

    clear_problem_elements = list(dict.fromkeys(problem_elements))
    # print("Проблемные элементы: ", clear_problem_elements)
    # print("Оценка: ", grade)

    msg = json.dumps(clear_problem_elements)  # [:] ??
    if grade == 1:
        return {'input_list': [{'ok': True, 'msg': msg, 'grade_decimal': 1}]}
    elif grade == 0:
        return {'input_list': [{'ok': False, 'msg': msg, 'grade_decimal': 0}]}
    else:
        return {'input_list': [{'ok': 'Partial', 'msg': msg, 'grade_decimal': grade}]}


student_data_json = json.dumps(student_data, ensure_ascii=False).replace("\"", "'")

answer_str = '{"answer":{"detail_6":{"type":"detail","id":"detail_6","title":"Деталь 6","height":1,"width":3,"x":17,"y":12},"detail_5":{"type":"detail","id":"detail_5","title":"Деталь 5","height":1,"width":3,"x":17,"y":13},"detail_4_3":{"type":"detail","id":"detail_4_3","title":"Деталь 4.3","height":1,"width":3,"x":14,"y":6},"detail_4_2":{"type":"detail","id":"detail_4_2","title":"Деталь 4.2","height":1,"width":2,"x":15,"y":7},"detail_4_1":{"type":"detail","id":"detail_4_1","title":"Деталь 4.1","height":1,"width":3,"x":14,"y":8},"node_4":{"type":"node","id":"node_4","title":"Узел 4","height":3,"width":3,"x":17,"y":6},"detail_3_3":{"type":"detail","id":"detail_3_3","title":"Деталь 3.3","height":1,"width":4,"x":10,"y":11},"detail_3_2":{"type":"detail","id":"detail_3_2","title":"Деталь 3.2","height":1,"width":1,"x":13,"y":10},"detail_3_1":{"type":"detail","id":"detail_3_1","title":"Деталь 3.1","height":1,"width":2,"x":12,"y":9},"node_3":{"type":"node","id":"node_3","title":"Узел 3","height":3,"width":6,"x":14,"y":9},"detail_2_3":{"type":"detail","id":"detail_2_3","title":"Деталь 2.3","height":1,"width":3,"x":8,"y":2},"detail_2_2":{"type":"detail","id":"detail_2_2","title":"Деталь 2.2","height":1,"width":3,"x":8,"y":1},"detail_2_1":{"type":"detail","id":"detail_2_1","title":"Деталь 2.1","height":1,"width":4,"x":7,"y":0},"node_2":{"type":"node","id":"node_2","title":"Узел 2","height":3,"width":5,"x":11,"y":0},"detail_1_3":{"type":"detail","id":"detail_1_3","title":"Деталь 1.3","height":1,"width":4,"x":8,"y":3},"detail_1_2":{"type":"detail","id":"detail_1_2","title":"Деталь 1.2","height":1,"width":2,"x":10,"y":5},"detail_1_1":{"type":"detail","id":"detail_1_1","title":"Деталь 1.1","height":1,"width":3,"x":9,"y":4},"node_1":{"type":"node","id":"node_1","title":"Узел 1","height":3,"width":4,"x":12,"y":3},"aggregate_1":{"type":"aggregate","id":"aggregate_1","title":"Аггрегат 1","height":6,"width":4,"x":16,"y":0},"machine_1":{"type":"machine","id":"machine_1","title":"Машина 1","height":14,"width":6,"x":20,"y":0}}}'
print(check_answer(1, answer_str))

