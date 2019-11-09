## -*- coding: utf-8 -*-

import logging
import sys
import time
import json
import demjson
import hashlib

source_str = """
{ msg_1: { type: "choice", text: "Что вы предпримите первым делом, чтобы выбраться скорее из леса живым и здоровым?", choices: [ { text: "Для начала остановлюсь и соберусь с мыслями", next_id: { condition: ["water_bottle"], yes: "msg_31", no: "msg_3" } }, { text: "Позвоню в МЧС", next_id: "msg_29" }, ], image: "odin_v_lesu.png" }, msg_2:{ type: "text", text: "Это хороший вариант. И ни в коем случае не сидите на холодной земле, она быстро заберет тепло вашего тела. Сотрудники МЧС найдут вас в самое ближайшее время.", final: true, success: true, image: "odin_v_lesu.png" }, msg_3: { type: "choice", text: "Постарайтесь успокоиться. Чтобы прийти в себя: визуализируйте свой страх, представьте его и как бы отойдите на шаг, посмотреть на него со стороны. Однако скоро стемнеет, но вы услышали шум машин. Пойдете на звук?", choices: [ { text: "Начну бегать по лесу, осматриваясь", next_id: "msg_32" }, { text: "Пойду на шум машин", next_id: "msg_9" }, ], image: "odin_v_lesu.png" }, msg_4:{ type: "text", text: "Это хороший вариант. И ни в коем случае не сидите на холодной земле, она быстро заберет тепло вашего тела. Сотрудники МЧС найдут вас в самое ближайшее время.", final: true, success: true, image: "odin_v_lesu.png" }, msg_5:{ type: "text", text: "Это хороший вариант. Ни в коем случае не сидите на холодной земле, она быстро заберет тепло вашего тела. Можете также развести огонь для тепла. Сотрудники МЧС найдут вас в самое ближайшее время.", final: true, success: true, image: "odin_v_lesu.png" }, msg_7:{ type: "text", text: "Плохой вариант. Если только вы слышите хоть какие-то звуки, двигайтесь на шум. Не можете идти ,ползите на шум. В случае, если вы съели смертельно-ядовитую ягоду, двигаться на шум - единственный шанс выйти на людей, которые помогут с оказанием квалифицированной медицинской помощи.", final: true, success: false, image: "odin_v_lesu.png" }, msg_9: { type: "choice", text: "Вы вышли на дорогу. Что дальше?", choices: [ { text: "Остановлю машину", next_id: "msg_17" }, { text: "Садиться в проезжающий автомобиль опасно. Пойду пешком вдоль дороги", next_id: "msg_16" }, ], image: "odin_v_lesu.png" }, msg_10: { type: "choice", text: "Верно! Нельзя тратить световой день на поиск еды. Надо действовать! Что дальше?", choices: [ { text: "Сделаю настил из веток, чтоб было мягче лежать. Отдохну", next_id: "msg_11" }, { text: "Пойду на шум машин", next_id: "msg_9" }, ], image: "odin_v_lesu.png" }, msg_11:{ type: "text", text: "Плохой вариант. Нельзя тратить световой день на отдых. Вы потеряете драгоценное время и силы.", final: true, success: false, image: "odin_v_lesu.png" }, msg_12: { type: "choice", text: "Молодец! Но если знакомых ягод не находится, как долго ты планируешь искать еду?", choices: [ { text: "Пока не найду", next_id: "msg_28" }, { text: "Не более 30 минут", next_id: "msg_10" }, ], image: "odin_v_lesu.png" }, msg_13: { type: "choice", text: "Вы встретили куст с привлекательными, но незнакомыми ягодами. Скушаете или нет?", choices: [ { text: "Съем, я очень голоден.", next_id: "msg_14" }, { text: "Не съем. Пойду искать знакомые ягоды", next_id: "msg_12" }, ], image: "odin_v_lesu.png" }, msg_14: { type: "choice", text: "Не стоит есть незнакомые ягоды. Вас стало подташнивать и начала кружиться голова. Вы слышите шум машин. Что будете делать?", choices: [ { text: "Присяду отдохнуть. Меня же тошнит", next_id: "msg_7" }, { text: "Пойду на шум машин", next_id: "msg_33" }, ], image: "odin_v_lesu.png" }, msg_16: { type: "choice", text: "Вы уже долго идете. Темнеет. Что будете делать?", choices: [ { text: "Остановлю машину", next_id: "msg_17" }, { text: "Не буду останавливать машину, это очень опасно. Пойду пешком вдоль дороги", next_id: "msg_34" }, ], image: "odin_v_lesu.png" }, msg_17: { type: "choice", text: "Машина остановилась. У вас есть шанс оценить водителя и салон на предмет подозрительности. Вы будете тратить на это время?", choices: [ { text: "Да, безопасность - превыше всего", comment: "Молодцы! Обратите внимание на взгляд, адекватность и связность речи водителя, руки (криминальные тату, характерные порезы). В салоне машины обратите внимание на запах, подозрительные пятна на сиденьях", next_id: "msg_19" }, { text: "Нет, я выбрался из леса! Что плохого со мной может случиться на людях?)", next_id: "msg_20" }, ], image: "odin_v_lesu.png" }, msg_19: { type: "choice", text: "Здорово! Но вот вы видите, что водитель не сильно приветлив, даже немного агрессивен. Сядете в этот автомобиль?", choices: [ { text: "Садиться к этому водителю опасно. Продолжу идти пешком вдоль дороги", next_id: "msg_16" }, { text: "Да, я выбрался из леса! Что плохого со мной может случиться на людях?", next_id: "msg_20" }, ], image: "odin_v_lesu.png" }, msg_20: { type: "choice", text: "Всё-таки стоило потратить время и оценить адекватность водителя. Вы понимаете, что едете куда-то не туда. Ваши действия?", choices: [ { text: "Включу актерское мастерство: изображу, что я неадекватный, сумасшедший, начну кричать, размахивать руками", next_id: "msg_23" }, { text: "Звоню другу: 1.Сообщаю номер авто, место, куда еду", next_id: "msg_21" }, ], image: "odin_v_lesu.png" }, msg_21:{ type: "text", text: "Это должно сработать. Явки/пароли вы сообщили. Будьте аккуратны и бдительны. Постарайтесь понять искренность намерений водителя помочь вам", final: true, success: true, image: "odin_v_lesu.png" }, msg_23: { type: "choice", text: "Это может сработать, и водитель даст вам шанс «убраться» из машины прямо сейчас. Вы выйдете?", choices: [ { text: "Конечно, так будет безопаснее", next_id: "msg_25" }, { text: "Нет, упрошу водителя всё-таки подбросить меня", next_id: "msg_26" }, ], image: "odin_v_lesu.png" }, msg_25:{ type: "text", text: "Бегите, как только появится такая возможность. Вы можете узнать у водителей проезжающих машин или людей, которых встретите, далеко ли до ближайшего населенного пункта, из которого вы сможете на автобусе доехать до своего дома", final: true, success: true, image: "odin_v_lesu.png" }, msg_26:{ type: "text", text: "Вы очень сильно рискуете попасть в руки опасного человека. Бегите, как только появится такая возможность.", final: true, success: false, image: "odin_v_lesu.png" }, msg_28:{ type: "text", text: "Плохой вариант. Нельзя тратить световой день на поиск еды. Вы потеряете драгоценное время и силы. ", final: true, success: false, image: "odin_v_lesu.png" }, msg_29: { type: "choice", text: "Сотрудники МЧС сказали вам, что нужно делать, но через обозначенное время они не вышли на вас. Ваши действия?", choices: [ { text: "Всё равно останусь ждать сотрудников МЧС. Я знаю, что мой звонок принят ими. Я с ними говорил, и они обещали найти меня", next_id: "msg_30" }, { text: "Начну бегать по лесу, осматриваясь.", next_id: "msg_32" }, ], image: "odin_v_lesu.png" }, msg_30: { type: "choice", text: "Это хороший вариант. Сотрудники МЧС найдут вас в самое ближайшее время. Но пока ждете, не стоит бездействовать! Чем займетесь?!", choices: [ { text: "Разведу огонь", next_id: "msg_2" }, { text: "Пойду на шум машин", next_id: "msg_9" }, ], image: "odin_v_lesu.png" }, msg_31: { type: "choice", text: "У вас есть с собой вода! Сделайте пару глотков, подышите глубоко. Чтобы прийти в себя: визуализируйте свой страх, представьте его и как бы отойдите на шаг, посмотреть на него со стороны. Однако скоро стемнеет, но вы услышали шум машин. Пойдете на звук?", choices: [ { text: "Начну бегать по лесу, осматриваясь.", next_id: "msg_32" }, { text: "Пойду на шум машин", next_id: "msg_9" }, ], image: "odin_v_lesu.png" }, msg_32: { type: "choice", text: "Окей, вы потратили драгоценные силы и время на хаотичные метания. Более того, вы ушли с места, где вас будут искать сотрудники МЧС. Что будете делать дальше?", choices: [ { text: "Разведу огонь и сообщу в МЧС о смене положения/вернусь в прежнее место локации", next_id: "msg_4" }, { text: "Пойду добывать себе еду", next_id: "msg_13" }, ], image: "odin_v_lesu.png" }, msg_33:{ type: "text", text: "Молодец! Если только вы слышите хоть какие-то звуки, двигайтесь на шум. Не можете идти ,ползите на шум. В случае, если вы съели смертельно-ядовитую ягоду, двигаться на шум - единственный шанс выйти на людей, которые помогут с оказанием квалифицированной медицинской помощи.", final: true, success: true, image: "odin_v_lesu.png" }, msg_34:{ type: "text", text: "Вы ушли с места, в котором вас будет искать МЧС. Еще и темнеет. Вы очень сильно рискуете. В данном случае стоило остаться на исходном месте и дожидаться сотрудников МЧС.", final: true, success: false, image: "odin_v_lesu.png" }, }
"""
source_obj = demjson.decode(source_str)


print(source_obj)

# source_obj_str = json.dumps(source_obj)
# student_salt = "salt"
# first_msg = "msg_1"
#
# # for key in source_obj.keys():
# #     hash_msg = hashlib.md5(str(key + student_salt).encode('utf-8')).hexdigest()
# #     source_obj_str = source_obj_str.replace('"' + key + '"', '"' + hash_msg + '"')
# # source_obj = json.loads(source_obj_str)
# # first_msg = hashlib.md5(str(first_msg + student_salt).encode('utf-8')).hexdigest()
#
# # print(source_obj)
#
# student_path = ["msg_1","msg_3", "msg_5"]
#
# things = [{"name":"wagter_bottle","html":"&#1052;&#1086;&#1076;&#1085;&#1099;&#1077; &#1082;&#1088;&#1086;&#1089;&#1089;&#1086;&#1074;&#1082;&#1080;","image_src":"sneakers.svg"},{"name":"pepsi","html":"&#1055;&#1077;&#1087;&#1089;&#1080; &#1082;&#1086;&#1083;&#1072; 0,5 &#1083;.","image_src":"pepsi.svg"},{"name":"matches","html":"&#1047;&#1072;&#1078;&#1080;&#1075;&#1072;&#1083;&#1082;&#1072; &#1080;&#1083;&#1080; &#1089;&#1087;&#1080;&#1095;&#1082;&#1080;","image_src":"matches.svg"}]
#
# # print(things)
# def get_next_id_list(item_key, obj, student_things):
#
#     def get_recursively(search_dict, field):
#         """
#         Takes a dict with nested lists and dicts,
#         and searches all dicts for a key of the field
#         provided.
#         """
#         fields_found = []
#
#         for key, value in search_dict.items():
#
#             if key == field:
#                 fields_found.append(value)
#
#             elif isinstance(value, dict):
#                 results = get_recursively(value, field)
#                 for result in results:
#                     fields_found.append(result)
#
#             elif isinstance(value, list):
#                 for item in value:
#                     if isinstance(item, dict):
#                         more_results = get_recursively(item, field)
#                         for another_result in more_results:
#                             fields_found.append(another_result)
#
#         return fields_found
#
#     finded = get_recursively(obj[item_key], 'next_id')
#     finded_list = []
#
#     things_names = [x['name'] for x in student_things]
#
#     for item in finded:
#         if isinstance(item, dict):
#
#             list_keys = list(item.keys())
#
#             if 'condition' in list_keys and 'yes' in list_keys and 'no' in list_keys:
#                 condition = item["condition"]
#                 yes = item["yes"]["next_id"]
#                 no = item["no"]["next_id"]
#
#                 if set(condition).issubset(set(things_names)):
#                     finded_list.append(yes)
#                 else:
#                     finded_list.append(no)
#             else:
#                 for sub_item in get_recursively(item, 'next_id'):
#                     print(item_key, " item: ", item, sub_item)
#                     finded_list.append(sub_item)
#         else:
#             finded_list.append(item)
#
#     return finded_list
#
#
# def get_grade(path, messages, first):
#     grade = 0
#
#     keep_on_process = True
#
#     # отсекаем путь раный нулю или с неправильным первым сообщением
#     if len(path) == 0:
#         keep_on_process = False
#     else:
#         if path[0] != first:
#             keep_on_process = False
#
#     # Не все сообщения из пути есть в ключах messages
#     if not set(path).issubset(messages.keys()):
#         keep_on_process = False
#
#     if keep_on_process and 'final' in messages[path[-1]]:
#         # print('существует поле "final"')
#         if messages[path[-1]]["final"]:
#             if messages[path[-1]]["success"]:
#                 grade = 1
#                 # print('финал успешный')
#             else:
#                 grade = 0
#                 # print('финал не успешный')
#         # else:
#         #     pass
#     # else:
#         # print('поле "final" не существует или длина пути равна нулю')
#         # pass
#
#     # если он дошел до этого этапа с единицей
#
#     if grade == 1:
#         # or grade == 0:
#         i = 0
#         for step in path:
#             if i+1 != len(path):
#                 if path[i+1] in get_next_id_list(step, messages, things):
#                     pass
#                 else:
#                     # print(path[i+1], ' не содержится в ', step, )  # messages[step]
#                     grade = 0
#             # else:
#             #     print('tyt poslednii', step)
#
#             i = i+1
#
#     return grade
#
#
# print("Оценка: ", get_grade(student_path, source_obj, first_msg))


