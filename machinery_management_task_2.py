import json

types = ["machine", "aggregate", "node", "detail"]

structure = {
    "type": "machine",
    "id": "machine_1",
    "duration": 6,
    "title": "Машина",
    "children": [
        {
            "type": "aggregate",
            "id": "aggregate_1",
            "duration": 4,
            "title": "Аггрегат",
            "children": [
                {
                    "type": "node",
                    "id": "node_1",
                    "duration": 4,
                    "title": "Узел 1",
                    "children": [
                        {
                            "type": "detail",
                            "id": "detail_1_1",
                            "duration": 3,
                            "title": "Деталь 1.1"
                        },
                        {
                            "type": "detail",
                            "id": "detail_1_2",
                            "duration": 2,
                            "title": "Деталь 1.2"
                        },
                        {
                            "type": "detail",
                            "id": "detail_1_3",
                            "duration": 4,
                            "title": "Деталь 1.3"
                        }
                    ]
                },
                {
                    "type": "node",
                    "id": "node_2",
                    "duration": 5,
                    "title": "Узел 2",
                    "children": [
                        {
                            "type": "detail",
                            "id": "detail_2_1",
                            "duration": 4,
                            "title": "Деталь 2.1"
                        },
                        {
                            "type": "detail",
                            "id": "detail_2_2",
                            "duration": 3,
                            "title": "Деталь 2.2"
                        },
                        {
                            "type": "detail",
                            "id": "detail_2_3",
                            "duration": 3,
                            "title": "Деталь 2.3"
                        }
                    ]
                },
            ]
        },
        {
            "type": "node",
            "id": "node_3",
            "duration": 6,
            "title": "Узел 3",
            "children": [
                {
                    "type": "detail",
                    "id": "detail_3_1",
                    "duration": 2,
                    "title": "Деталь 3.1"
                },
                {
                    "type": "detail",
                    "id": "detail_3_2",
                    "duration": 1,
                    "title": "Деталь 3.2"
                },
                {
                    "type": "detail",
                    "id": "detail_3_3",
                    "duration": 4,
                    "title": "Деталь 3.3"
                }
            ]
        },
        {
            "type": "node",
            "id": "node_4",
            "duration": 3,
            "title": "Узел 4",
            "children": [
                {
                    "type": "detail",
                    "id": "detail_4_1",
                    "duration": 3,
                    "title": "Деталь 4.1"
                },
                {
                    "type": "detail",
                    "id": "detail_4_2",
                    "duration": 2,
                    "title": "Деталь 4.2"
                },
                {
                    "type": "detail",
                    "id": "detail_4_3",
                    "duration": 3,
                    "title": "Деталь 4.3"
                }
            ]
        },
        {
            "type": "detail",
            "id": "detail_5",
            "duration": 3,
            "title": "Деталь 5"
        },
        {
            "type": "detail",
            "id": "detail_6",
            "duration": 3,
            "title": "Деталь 6"
        }
    ]
}

# print(structure)
list = []


def get_list_from_structure(structure):
    def get_elem(elem, current_d):
        tmp_obj = {
            "type": elem["type"],
            "id": elem["id"],
            "duration": elem["duration"],
            "title": elem["title"],
            "end_on": elem["duration"] + current_d
        }
        list.append(tmp_obj)
        if "children" in elem.keys():
            for x in elem['children']:
                get_elem(x, tmp_obj["end_on"])

    get_elem(structure, 0)


get_list_from_structure(structure)

extra_cells_count = 6

details = [x for x in list if x['type'] == 'detail']
area_height = len(details)
area_width = max([x['end_on'] for x in details]) + extra_cells_count
# print("Высота площадки: ", area_height, "\nШирина площадки: ", area_width)


# print(list)

problem_elements = []
answer_str = '{"answer":{"detail_6":{"type":"detail","id":"detail_6","title":"Деталь 6","height":1,"width":3,"x":16,"y":13},"detail_5":{"type":"detail","id":"detail_5","title":"Деталь 5","height":1,"width":3,"x":16,"y":12},"detail_4_3":{"type":"detail","id":"detail_4_3","title":"Деталь 4.3","height":1,"width":3,"x":0,"y":11},"detail_4_2":{"type":"detail","id":"detail_4_2","title":"Деталь 4.2","height":1,"width":3,"x":6,"y":9},"detail_4_1":{"type":"detail","id":"detail_4_1","title":"Деталь 4.1","height":1,"width":2,"x":6,"y":2},"node_4":{"type":"node","id":"node_4","title":"Узел 4","height":3,"width":3,"x":16,"y":3},"detail_3_3":{"type":"detail","id":"detail_3_3","title":"Деталь 3.3","height":1,"width":3,"x":0,"y":7},"detail_3_2":{"type":"detail","id":"detail_3_2","title":"Деталь 3.2","height":1,"width":3,"x":0,"y":6},"detail_3_1":{"type":"detail","id":"detail_3_1","title":"Деталь 3.1","height":1,"width":3,"x":6,"y":1},"node_3":{"type":"node","id":"node_3","title":"Узел 3","height":3,"width":6,"x":13,"y":0},"detail_2_3":{"type":"detail","id":"detail_2_3","title":"Деталь 2.3","height":1,"width":3,"x":0,"y":3},"detail_2_2":{"type":"detail","id":"detail_2_2","title":"Деталь 2.2","height":1,"width":3,"x":0,"y":2},"detail_2_1":{"type":"detail","id":"detail_2_1","title":"Деталь 2.1","height":1,"width":3,"x":0,"y":1},"node_2":{"type":"node","id":"node_2","title":"Узел 2","height":1,"width":3,"x":0,"y":0},"detail_1_3":{"type":"detail","id":"detail_1_3","title":"Деталь 1.3","height":1,"width":3,"x":3,"y":13},"detail_1_2":{"type":"detail","id":"detail_1_2","title":"Деталь 1.2","height":1,"width":3,"x":8,"y":5},"detail_1_1":{"type":"detail","id":"detail_1_1","title":"Деталь 1.1","height":1,"width":1,"x":9,"y":7},"node_1":{"type":"node","id":"node_1","title":"Узел 1","height":2,"width":6,"x":5,"y":11},"aggregate_1":{"type":"aggregate","id":"aggregate_1","title":"Аггрегат 1","height":6,"width":4,"x":15,"y":6},"machine_1":{"type":"machine","id":"machine_1","title":"Машина 1","height":14,"width":6,"x":19,"y":0}}}'


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

# def


def get_element_children(student_obj, element):
    ret_list = []
    for k in student_obj.keys():
        if student_obj[k]['x']+student_obj[k]['width'] == element['x']:
            ret_list.append(student_obj[k])
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
    return not (a_coords['y'] <= b_coords['y1'] or a_coords['y1'] >= b_coords['y'] or a_coords['x1'] <= b_coords['x'] or a_coords['x'] >= b_coords['x1'])


def check_children_intersections(children_list):
    no_intersect = True
    for child in children_list:
        for child_1 in children_list:
            if child["id"] != child_1["id"]:
                pass
                if intersects(child, child_1):
                    print("Нашли пересечение: ", child["id"])
                    problem_elements.append(child["id"])
                    no_intersect = False
                    return no_intersect
    return no_intersect


def check_children_widths(student_obj, correct_children):
    for child in correct_children:
        if child["duration"] != student_obj[child["id"]]["width"]:
            print("Нашли разные длины: ", child["id"])
            problem_elements.append(child["id"])
            return False
    return True


def check_children_heights(student_obj, correct_children):
    for child in correct_children:
        if get_details_count(child) != student_obj[child["id"]]["height"]:
            print("Нашли разные высоты: ", child["id"])
            problem_elements.append(child["id"])
            return False
    return True

def check_children_equal(student_children, correct_children):

    correct_children_1 = ['detail_6', 'detail_5', 'node_4', 'node_3']
    student_children_1 = ['detail_6', 'detail_5', 'node_4', 'node_3', 'aggregate_1']

    print( list((set(correct_children_1) - set(student_children_1))))
    print( (set(student_children_1) - set(correct_children_1)))

    if len(set(student_children)) == len(set(correct_children)):
        return True
    else:
        print("Массивы не равны")
        return False


def check(ans):
    answer_obj = json.loads(ans)["answer"]

    user_machine = answer_obj[structure["id"]]

    if user_machine['width'] == structure["duration"] and user_machine['x'] == area_width - extra_cells_count and user_machine['y'] == 0 and user_machine['height'] == area_height:

        def rec_check(student_el, cor_obj):

            # print(student_el)
            # print(cor_obj)

            children_ids_student = [x["id"] for x in get_element_children(answer_obj, student_el)]
            children_ids_correct = [x["id"] for x in cor_obj['children']]

            if check_children_equal(children_ids_student, children_ids_correct) and check_children_intersections([answer_obj[x] for x in children_ids_student]) and check_children_widths(answer_obj, cor_obj["children"]) and check_children_heights(answer_obj, cor_obj["children"]):
                print("poka ok")
                # if
            else:
                print("choto ne ok")

        rec_check(user_machine, structure)

        # print(intersects(answer_obj['aggregate_1'], answer_obj['node_1']) ,answer_obj['aggregate_1'], answer_obj['node_1'])

        # prev = area_width - extra_cells_count - 1
        # print(prev)
        # for l in [x['id'] for x in structure["children"]]:
        #     print(answer_obj[l])
        #     point_in_el({"x": prev, "y": 1}, answer_obj[l])
        #     pass

    else:
        problem_elements.append(structure["id"])

    print("Проблемные элементы: ", problem_elements)


check(answer_str)

# for l in details:
#     print(l)
# print(len(details))
# print(list(filtered))
