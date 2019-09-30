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

answer_str = '{"answer":{"detail_6":{"type":"detail","id":"detail_6","title":"Деталь 6","height":1,"width":3,"x":0,"y":13},"detail_5":{"type":"detail","id":"detail_5","title":"Деталь 5","height":1,"width":3,"x":0,"y":12},"detail_4_3":{"type":"detail","id":"detail_4_3","title":"Деталь 4.3","height":1,"width":3,"x":0,"y":11},"detail_4_2":{"type":"detail","id":"detail_4_2","title":"Деталь 4.2","height":1,"width":3,"x":0,"y":10},"detail_4_1":{"type":"detail","id":"detail_4_1","title":"Деталь 4.1","height":1,"width":3,"x":0,"y":9},"node_4":{"type":"node","id":"node_4","title":"Узел 4","height":1,"width":3,"x":0,"y":8},"detail_3_3":{"type":"detail","id":"detail_3_3","title":"Деталь 3.3","height":1,"width":3,"x":0,"y":7},"detail_3_2":{"type":"detail","id":"detail_3_2","title":"Деталь 3.2","height":1,"width":3,"x":0,"y":6},"detail_3_1":{"type":"detail","id":"detail_3_1","title":"Деталь 3.1","height":1,"width":3,"x":0,"y":5},"node_3":{"type":"node","id":"node_3","title":"Узел 3","height":1,"width":3,"x":0,"y":4},"detail_2_3":{"type":"detail","id":"detail_2_3","title":"Деталь 2.3","height":1,"width":3,"x":0,"y":3},"detail_2_2":{"type":"detail","id":"detail_2_2","title":"Деталь 2.2","height":1,"width":3,"x":0,"y":2},"detail_2_1":{"type":"detail","id":"detail_2_1","title":"Деталь 2.1","height":1,"width":3,"x":0,"y":1},"node_2":{"type":"node","id":"node_2","title":"Узел 2","height":1,"width":4,"x":5,"y":6},"detail_1_3":{"type":"detail","id":"detail_1_3","title":"Деталь 1.3","height":1,"width":3,"x":3,"y":13},"detail_1_2":{"type":"detail","id":"detail_1_2","title":"Деталь 1.2","height":1,"width":3,"x":3,"y":12},"detail_1_1":{"type":"detail","id":"detail_1_1","title":"Деталь 1.1","height":1,"width":3,"x":3,"y":11},"node_1":{"type":"node","id":"node_1","title":"Узел 1","height":1,"width":3,"x":3,"y":10},"aggregate_1":{"type":"aggregate","id":"aggregate_1","title":"Аггрегат","height":1,"width":3,"x":16,"y":0},"machine_1":{"type":"machine","id":"machine_1","title":"Машина","height":14,"width":6,"x":19,"y":0}}}'


def all_params_equal(obj_1, obj_2, params):
    for param in params:
        if obj_1[param] != obj_2[param]:
            return False
    return True

# def point_in_el(point, element):
#     print(point)
#     if point['x'] >= element["x"] and point['x'] <= (element["x"]+element["width"]) and point['y'] >= element["height"] and point['y'] <= element["height"]+element["y"]:
#         print('Принадлежит')
#     else:
#         print('Не принадлежит')

def check(ans):
    answer_obj = json.loads(ans)["answer"]
    problem_elements = []
    user_machine = answer_obj[structure["id"]]

    if user_machine['width'] == structure["duration"] and user_machine['x'] == area_width - extra_cells_count and user_machine['y'] == 0 and user_machine['height'] == area_height:

        # print(user_machine['x'])
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
