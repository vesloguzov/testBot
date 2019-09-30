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


def filter_details(elemet):
    el_type = 'detail'
    if elemet['type'] == el_type:
        return True
    else:
        return False


get_list_from_structure(structure)


details = [x for x in list if x['type'] == 'detail']
area_height = len(details)
area_width = max([x['end_on'] for x in details])
print("Высота площадки: ", area_height, "\nШирина площадки: ", area_width)


print(list)
# for l in details:
#     print(l)
# print(len(details))
# print(list(filtered))

