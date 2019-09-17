## -*- coding: utf-8 -*-

import logging
import sys
import time
import json
import demjson
import hashlib

source_str = """
{
        msg_1: {
            type: "choice",
            text: "Конец сентября. Ты пошел в лес за грибами. Потерял ориентиры, заблудился. У тебя с собой пластиковая бутылка 0,5л., воды осталось на один глоток на дне бутылки. Еды нет. Есть мобильный телефон. Но нет денежных средств и отложенного платежа. От населенного пункта 3 км, но ты про это не знаешь. Недалеко(1 км.) находится автомобильная трасса. Слышно на расстоянии шум моторов. ",
            choices: [
                {
                    text: "Для начала остановлюсь и соберусь с мыслями",
                    next_id:
                        {
                            condition: ["water_bottle"],
                            yes: { next_id: "msg_2"},
                            no: { next_id: "msg_3"}
                        },
                    comment: "КОММЕНТАРИЙ (Для начала остановлюсь и соберусь с мыслями)"
                },
                {
                    text: "Позвоню в МЧС",
                    next_id: "msg_4",
                    comment: "КОММЕНТАРИЙ (Позвоню в МЧС)"
                },
            ],
            image:"msg_1.jpg"
        },
        msg_2: {
            type: "choice",
            text: "У вас есть с собой вода! Сделайте пару глотков, подышите глубоко. Чтобы прийти в себя: визуализируйте свой страх, представьте его и как бы отойдите на шаг, посмотреть  на него со стороны. Однако скоро стемнеет, но вы услышали шум машин. Пойдете на звук?",
            choices: [
                {
                    text: "Начну бегать по лесу, осматриваясь.",
                    next_id: "msg_8"
                },
                {
                    text: "Пойду на шум машин",
                    next_id: "msg_9"
                },
            ]
        },
        msg_3: {
            type: "choice",
            text: "Постарайтесь успокоиться. Чтобы прийти в себя: визуализируйте свой страх, представьте его и как бы отойдите на шаг, посмотреть  на него со стороны. Однако скоро стемнеет, но вы услышали шум машин. Пойдете на звук?",
            choices: [
                {
                    text: "Начну бегать по лесу, осматриваясь.",
                    next_id: "msg_8"
                },
                {
                    text: "Пойду на шум машин",
                    next_id: "msg_9"
                },
            ],
            // image:"msg_1.jpg"
        },
        msg_4: {
            type: "choice",
            text: "Сотрудники МЧС сказали вам, что нужно делать, но через обозначенное время они не вышли на вас. Ваши действия?",
            choices: [
                {
                    text: "Всё равно останусь ждать сотрудников МЧС. Я знаю, что мой звонок принят ими. Я с ними говорил, и они обещали найти меня",
                    next_id:
                        {
                            condition: ["energy_bar"],
                            yes: { next_id: "msg_5"},
                            no: { next_id: "msg_6"}
                        }
                },
                {
                    text: "Начну бегать по лесу, осматриваясь",
                    next_id: "msg_8"
                }, {
                    text: "Пойду на шум машин",
                    next_id: "msg_9"
                },
            ],
            image:"msg_4.jpg"
        },
        msg_5: {
            type: "text",
            text: "Это хороший вариант. Сотрудники МЧС найдут вас в самое ближайшее время. Можете во время ожидания развести огонь для тепла, сделать настил из веток, чтобы отдохнуть. Ни в коем случае не сидите на холодной земле, она быстро заберет тепло вашего тела. У вас к тому же есть энергетический батончик. Подкрепитесь!",
            final: true,
            success: true,
            image:"msg_5_6.jpg"
        },
        msg_6: {
            type: "text",
            text: "Это хороший вариант. Сотрудники МЧС найдут вас в самое ближайшее время. Можете во время ожидания развести огонь для тепла, сделать настил из веток, чтобы отдохнуть. Ни в коем случае не сидите на холодной земле, она быстро заберет тепло вашего тела",
            final: true,
            success: true,
            image:"msg_5_6.jpg"
        },
        msg_7: {
            type: "text",
            text: "Плохой вариант. Если только вы слышите хоть какие-то звуки, двигайтесь на шум. Не можете идти ,ползите на шум. В случае, если вы съели смертельно-ядовитую ягоду, двигаться на шум - единственный шанс выйти на людей, которые помогут с оказанием квалифицированной медицинской помощи. Пройдите тренажер заново!",
            final: true,
            success: false,
            image:"msg_7.jpg"
        },
        msg_8: {
            type: "choice",
            text: "Окей, вы потратили драгоценные силы и время на хаотичные метания. Что будете делать дальше?",
            choices: [
                {
                    text: "У меня есть энергетический батончик! Я подкреплюсь!",
                    next_id: "msg_27",
                    condition: ["energy_bar"]
                },
                {
                    text: "Пойду на шум машин",
                    next_id: "msg_9"
                },
                {
                    text: "Пойду добывать себе еду",
                    next_id: "msg_13"
                },
            ],
            image:"msg_8.jpg"
        },
        msg_9: {
            type: "choice",
            text: "Вы вышли на дорогу. Будете ли вы останавливать машину?",
            choices: [
                {
                    text: "Да",
                    next_id: "msg_17"
                },
                {
                    text: "Нет, это очень опасно. Пойду пешком вдоль дороги",
                    next_id: "msg_16"
                },
            ],
            image:"msg_9.jpg"
        },
        msg_10:{
            type: "choice",
            text: "Верно! Нельзя тратить световой день на поиск еды. Надо действовать! Что дальше?",
            choices: [
                {
                    text: "Сделаю настил из веток, чтоб было мягче лежать. Отдохну",
                    next_id: "msg_11"
                },
                {
                    text: "Пойду на шум машин",
                    next_id: "msg_9"
                },
            ],
            image:"msg_10_28.jpg"
        },
        msg_11:{
            type: "text",
            text: "Плохой вариант. Нельзя тратить световой день на отдых. Вы потеряете драгоценное время и силы. Пройдите тренажер заново!",
            final: true,
            success: false,
        },
        msg_12:{
            type: "choice",
            text: "Молодец! Но если знакомых ягод не находится, как долго ты планируешь искать еду?",
            choices: [
                {
                    text: "Пока не найду",
                    next_id: "msg_28"
                },
                {
                    text: "Не более 30 минут",
                    next_id: "msg_10"
                },
            ],
            image:"msg_12.jpg"
        },
        msg_13:{
            type: "choice",
            text: "Вы встретили куст с привлекательными ягодами (Описать их) Скушаете или нет?",
            choices: [
                {
                    text: "Съем, я очень голоден.",
                    next_id: "msg_14"
                },
                {
                    text: "Не съем. Пойду искать знакомые ягоды",
                    next_id: "msg_12"
                },
            ],
            image:"msg_13.jpg"
        },
        msg_14:{
            type: "choice",
            text: "Не стоит есть незнакомые ягоды. Вас стало подташнивать и начала кружиться голова. Вы слышите шум машин. Что будете делать?",
            choices: [
                {
                    text: "Присяду отдохнуть. Меня же тошнит",
                    next_id: "msg_7"
                },
                {
                    text: "Пойду на шум машин",
                    next_id: "msg_9"
                },
            ],
            image:"msg_14.jpg"
        },
        msg_15:{
            type: "choice",
            text: "Вы взяли с собой энергетический батончик. Подкрепитесь! Машина остановилась. У вас есть шанс оценить водителя и салон на предмет подозрительности. Вы будете тратить на это время?",
            choices: [
                {
                    text: "Нет, я выбрался из леса! Что плохого со мной может случиться на людях?)",
                    next_id: "msg_20"
                },
                {
                    text: "Да, безопасность - превыше всего",
                    next_id: "msg_19"
                },
            ],
            image:"msg_15_17.jpg",
        },
        msg_16:{
            type: "choice",
            text: "И долго будете идти?",
            choices: [
                {
                    text: "Пока не устану. Тогда начну останавливать проезжающие машины",
                    next_id: "msg_17"
                },
                {
                    text: "До ближайшего населенного пункта",
                    next_id: "msg_22"
                },
            ],
            image:"msg_16.jpg",
        },
        msg_17:{
            type: "choice",
            text: "Машина остановилась. У вас есть шанс оценить водителя и салон на предмет подозрительности. Вы будете тратить на это время?",
            choices: [
                {
                    text: "Да, безопасность - превыше всего",
                    next_id: "msg_19"
                },
                {
                    text: "Нет, я выбрался из леса! Что плохого со мной может случиться на людях?)",
                    next_id: "msg_20"
                },
            ],
            image:"msg_15_17.jpg",
        },
        msg_18:{
            type: "text",
            text: "Водитель оказался отличным парнем и довез вас до самого дома",
            final: true,
            success: true,
        },
        msg_19:{
            type: "choice",
            text: "Здорово! Но вот вы видите, что водитель не сильно приветлив, даже немного агрессивен. Сядете в автомобиль??",
            choices: [
                {
                    text: "Да, я выбрался из леса! Что плохого со мной может случиться на людях?)",
                    next_id: "msg_20"
                },
                {
                    text: "Нет, это очень опасно. Пойду пешком вдоль дороги",
                    next_id: "msg_16"
                },
            ],
            image:"msg_19_24.jpg",
        },
        msg_20:{
            type: "choice",
            text: "Всё-таки стоило потратить время и оценить адекватность водителя. Вы понимаете, что едете куда-то не туда. Ваши действия?",
            choices: [
                {
                    text: "Начну кричать на водителя, размахивать руками и пытаться выйти на ходу",
                    next_id: "msg_23"
                },
                {
                    text: "Звоню другу: 1.Сообщаю номер авто, место, куда еду",
                    next_id: "msg_21"
                },
            ]
        },
        msg_21:{
            type: "text",
            text: "Это должно сработать. Явки/пароли вы сообщили. Будьте аккуратны и бдительны. Постарайтесь понять искренность намерений водителя помочь вам",
            final: true,
            success: true,
            image:"msg_21.jpg",
        },
        msg_22:{
            type: "text",
            text: "Это хороший вариант. Главное, чтобы вам хватило сил и светового дня дойти до населенного пункта",
            final: true,
            success: true,
            image:"msg_22.jpg",
        },
        msg_23:{
            type: "choice",
            text: "Это не помогает. Что же делать?",
            choices: [
                {
                    text: "НИЧЕГО",
                    next_id: "msg_24"
                },
            ]
        },
        msg_24:{
            type: "choice",
            text: "Водитель дает вам шанс «убраться» из машины прямо сейчас. Вы выйдете?",
            choices: [
                {
                    text: "Конечно, так будет безопаснее",
                    next_id: "msg_25"
                },
                {
                    text: "Нет, упрошу водителя всё-таки подбросить меня",
                    next_id: "msg_26"
                },
            ],
            image:"msg_19_24.jpg",
        },
        msg_25:{
            type: "text",
            text: "Бегите, как только появится такая возможность. Вы можете узнать у водителей проезжающих машин или людей, которых встретите, далеко ли до ближайшего населенного пункта, из которого вы сможете на автобусе доехать до своего дома",
            final: true,
            success: true,
            image:"msg_25_26.jpg",
        },
        msg_26:{
            type: "text",
            text: "Вы очень сильно рискуете попасть в руки опасного человека. Бегите, как только появится такая возможность. И пройдите тренажер заново.",
            final: true,
            success: false,
            image:"msg_25_26.jpg",
        },
        msg_27:{
            type: "choice",
            text: "Подкрепились. Что  дальше?",
            choices: [
                {
                    text: "Сделаю настил из веток, чтоб было мягче лежать. Отдохну",
                    next_id: "msg_11"
                },
                {
                    text: "Пойду на шум машин",
                    next_id: "msg_9"
                },
            ],
            image:"msg_27.jpg",
        },
        msg_28:{
            type: "text",
            text: "Плохой вариант. Нельзя тратить световой день на поиск еды. Вы потеряете драгоценное время и силы. Пройдите тренажер заново!",
            final: true,
            success: false,
            image:"msg_10_28.jpg"
        },
    }
    """
source_obj = demjson.decode(source_str)

# print(source_obj)

source_obj_str = json.dumps(source_obj)
student_salt = "salt"
first_msg = "msg_1"

# for key in source_obj.keys():
#     hash_msg = hashlib.md5(str(key + student_salt).encode('utf-8')).hexdigest()
#     source_obj_str = source_obj_str.replace('"' + key + '"', '"' + hash_msg + '"')
# source_obj = json.loads(source_obj_str)
# first_msg = hashlib.md5(str(first_msg + student_salt).encode('utf-8')).hexdigest()

# print(source_obj)

student_path = ["msg_1","msg_3", "msg_5"]

things = [{"name":"wagter_bottle","html":"&#1052;&#1086;&#1076;&#1085;&#1099;&#1077; &#1082;&#1088;&#1086;&#1089;&#1089;&#1086;&#1074;&#1082;&#1080;","image_src":"sneakers.svg"},{"name":"pepsi","html":"&#1055;&#1077;&#1087;&#1089;&#1080; &#1082;&#1086;&#1083;&#1072; 0,5 &#1083;.","image_src":"pepsi.svg"},{"name":"matches","html":"&#1047;&#1072;&#1078;&#1080;&#1075;&#1072;&#1083;&#1082;&#1072; &#1080;&#1083;&#1080; &#1089;&#1087;&#1080;&#1095;&#1082;&#1080;","image_src":"matches.svg"}]

# print(things)
def get_next_id_list(item_key, obj, student_things):

    def get_recursively(search_dict, field):
        """
        Takes a dict with nested lists and dicts,
        and searches all dicts for a key of the field
        provided.
        """
        fields_found = []

        for key, value in search_dict.items():

            if key == field:
                fields_found.append(value)

            elif isinstance(value, dict):
                results = get_recursively(value, field)
                for result in results:
                    fields_found.append(result)

            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        more_results = get_recursively(item, field)
                        for another_result in more_results:
                            fields_found.append(another_result)

        return fields_found

    finded = get_recursively(obj[item_key], 'next_id')
    finded_list = []

    things_names = [x['name'] for x in student_things]

    for item in finded:
        if isinstance(item, dict):

            list_keys = list(item.keys())

            if 'condition' in list_keys and 'yes' in list_keys and 'no' in list_keys:
                condition = item["condition"]
                yes = item["yes"]["next_id"]
                no = item["no"]["next_id"]

                if set(condition).issubset(set(things_names)):
                    finded_list.append(yes)
                else:
                    finded_list.append(no)
            else:
                for sub_item in get_recursively(item, 'next_id'):
                    print(item_key, " item: ", item, sub_item)
                    finded_list.append(sub_item)
        else:
            finded_list.append(item)

    return finded_list


def get_grade(path, messages, first):
    grade = 0

    keep_on_process = True

    # отсекаем путь раный нулю или с неправильным первым сообщением
    if len(path) == 0:
        keep_on_process = False
    else:
        if path[0] != first:
            keep_on_process = False

    # Не все сообщения из пути есть в ключах messages
    if not set(path).issubset(messages.keys()):
        keep_on_process = False

    if keep_on_process and 'final' in messages[path[-1]]:
        # print('существует поле "final"')
        if messages[path[-1]]["final"]:
            if messages[path[-1]]["success"]:
                grade = 1
                # print('финал успешный')
            else:
                grade = 0
                # print('финал не успешный')
        # else:
        #     pass
    # else:
        # print('поле "final" не существует или длина пути равна нулю')
        # pass

    # если он дошел до этого этапа с единицей

    if grade == 1:
        # or grade == 0:
        i = 0
        for step in path:
            if i+1 != len(path):
                if path[i+1] in get_next_id_list(step, messages, things):
                    pass
                else:
                    # print(path[i+1], ' не содержится в ', step, )  # messages[step]
                    grade = 0
            # else:
            #     print('tyt poslednii', step)

            i = i+1

    return grade


print("Оценка: ", get_grade(student_path, source_obj, first_msg))


