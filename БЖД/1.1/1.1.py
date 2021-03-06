# -*- coding: utf-8 -*-
import random

variants = [
    {
    "q_title_1": u"В начале лета начали проводиться работы по перекладке асфальта на проезжей части магистральной улицы города без остановки потока движения транспорта.",
    "q_title_2": u"Какие виды опасностей присутствуют в зоне проведения ремонта:",

    "q_answer_1": "A",
    "q_answer_2": "A",
    "q_answer_3": "A",
    "q_answer_4": "A",
    "q_answer_5": "A",
    "q_answer_6": "A"
    },
    {
        "q_title_1": u"При перевозке азотной кислоты в цистерне грузового автомобиля произошла автомобильная авария.",
        "q_title_2": u"Какие виды опасностей присутствуют в зоне автомобильной аварии:",

        "q_answer_1": "B",
        "q_answer_2": "C",
        "q_answer_3": "B",
        "q_answer_4": "A",
        "q_answer_5": "A",
        "q_answer_6": "A"
    },
    {
        "q_title_1": u"При проведении строительных работ на территории жилой застройки тракторист Степанов повредил трубу газопровода.",
        "q_title_2": u"Какие виды опасностей присутствуют в зоне аварии газопровода:",

        "q_answer_1": "B",
        "q_answer_2": "B",
        "q_answer_3": "B",
        "q_answer_4": "A",
        "q_answer_5": "A",
        "q_answer_6": "A"
    },
    {
        "q_title_1": u"При проведении праздничных мероприятий посвящённых дню города было принято решение произвести фейерверк в центральном парке.",
        "q_title_2": u"Какие виды опасностей присутствуют в зоне проведения прозаичного фейерверка:",

        "q_answer_1": "B",
        "q_answer_2": "B",
        "q_answer_3": "A",
        "q_answer_4": "A",
        "q_answer_5": "A",
        "q_answer_6": "E"
    },
    {
        "q_title_1": u"В летние каникулы было принято решение организовать палаточный лагерь для отдыха студентов в пойме реки Чусовая.",
        "q_title_2": u"Какие виды опасностей присутствуют в зоне организации палаточного лагеря:",

        "q_answer_1": "D",
        "q_answer_2": "C",
        "q_answer_3": "C",
        "q_answer_4": "A",
        "q_answer_5": "A",
        "q_answer_6": "E"
    },
    {
        "q_title_1": u"При проведении лабораторных работ по физике студенты работают с различными приборами, подключенными к сети электропитания 220 В.",
        "q_title_2": u"Какие виды опасностей присутствуют при проведении лабораторных работ:",

        "q_answer_1": "B",
        "q_answer_2": "B",
        "q_answer_3": "A",
        "q_answer_4": "A",
        "q_answer_5": "A",
        "q_answer_6": "E"
    },
    {
        "q_title_1": u"При проведении лабораторных работ по Химии студенты работают с различными химическими реактивами, едкими и токсичными веществами.",
        "q_title_2": u"Какие виды опасностей присутствуют в зоне проведения лабораторных работ:",

        "q_answer_1": "B",
        "q_answer_2": "C",
        "q_answer_3": "B",
        "q_answer_4": "A",
        "q_answer_5": "A",
        "q_answer_6": "E"
    },
    {
        "q_title_1": u"На установке по вакуумной перегонке нефти на одном из нефтехимических заводов произошёл неконтролируемый выброс токсичного и взрывоопасного вещества.",
        "q_title_2": u"Какие виды опасностей присутствуют в зоне аварии:",

        "q_answer_1": "A",
        "q_answer_2": "B",
        "q_answer_3": "B",
        "q_answer_4": "A",
        "q_answer_5": "A",
        "q_answer_6": "E"
    },
    {
        "q_title_1": u"На полигоне по захоронению твердых бытовых отходов города Екатеринбурга в летний период произошло возгорание мусора.",
        "q_title_2": u"Какие виды опасностей присутствуют в зоне вокруг полигона:",

        "q_answer_1": "C",
        "q_answer_2": "A",
        "q_answer_3": "B",
        "q_answer_4": "B",
        "q_answer_5": "B",
        "q_answer_6": "C"
    },
    {
        "q_title_1": u"При проведении санкционированного митинга на площади города группа молодых людей стала призывать к противоправным действиям.",
        "q_title_2": u"Какие виды опасностей присутствуют в зоне проведения митинга:",

        "q_answer_1": "B",
        "q_answer_2": "A",
        "q_answer_3": "D",
        "q_answer_4": "A",
        "q_answer_5": "A",
        "q_answer_6": "D"
    }]

variant = random.choice(variants)

title_1 = variant["q_title_1"]
title_2 = variant["q_title_2"]

q_1_variant_A = True if variant["q_answer_1"] == "A" else False
q_1_variant_B = True if variant["q_answer_1"] == "B" else False
q_1_variant_C = True if variant["q_answer_1"] == "C" else False
q_1_variant_D = True if variant["q_answer_1"] == "D" else False

q_2_variant_A = True if variant["q_answer_2"] == "A" else False
q_2_variant_B = True if variant["q_answer_2"] == "B" else False
q_2_variant_C = True if variant["q_answer_2"] == "C" else False
q_2_variant_D = True if variant["q_answer_2"] == "D" else False

q_3_variant_A = True if variant["q_answer_3"] == "A" else False
q_3_variant_B = True if variant["q_answer_3"] == "B" else False
q_3_variant_C = True if variant["q_answer_3"] == "C" else False
q_3_variant_D = True if variant["q_answer_3"] == "D" else False

q_4_variant_A = True if variant["q_answer_4"] == "A" else False
q_4_variant_B = True if variant["q_answer_4"] == "B" else False

q_5_variant_A = True if variant["q_answer_5"] == "A" else False
q_5_variant_B = True if variant["q_answer_5"] == "B" else False

q_6_variant_A = True if variant["q_answer_6"] == "A" else False
q_6_variant_B = True if variant["q_answer_6"] == "B" else False
q_6_variant_C = True if variant["q_answer_6"] == "C" else False
q_6_variant_D = True if variant["q_answer_6"] == "D" else False
q_6_variant_E = True if variant["q_answer_6"] == "E" else False

print(q_1_variant_A)
print(q_1_variant_B)
print(q_1_variant_C)
print(q_1_variant_D)
print("----------------------------")
print(q_2_variant_A)
print(q_2_variant_B)
print(q_2_variant_C)
print(q_2_variant_D)
print("----------------------------")
print(q_3_variant_A)
print(q_3_variant_B)
print(q_3_variant_C)
print(q_3_variant_D)
print("----------------------------")
print(q_4_variant_A)
print(q_4_variant_B)
print("----------------------------")
print(q_5_variant_A)
print(q_5_variant_B)
print("----------------------------")
print(q_6_variant_A)
print(q_6_variant_B)
print(q_6_variant_C)
print(q_6_variant_D)
print(q_6_variant_E)