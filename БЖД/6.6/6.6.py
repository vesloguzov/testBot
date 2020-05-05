import random

variants = [{
    "title": u"при поступлении на работу", "answer": "C"},
    {"title": u"впервые на рабочем месте", "answer": "F"},
    {"title": u"на рабочем месте с установленной  нормативными документами периодичностью", "answer": "E"},
    {"title": u"при внесении изменений в инструкции, нарушении правил охраны труда, длительных перерывах в работе", "answer": "D"},
    {"title": u"при выполнении работ по наряду - допуску", "answer": "B"},
]

variant = random.choice(variants)

title = variant["title"]

A_answer = True if variant["answer"] == "A" else False
B_answer = True if variant["answer"] == "B" else False
C_answer = True if variant["answer"] == "C" else False
D_answer = True if variant["answer"] == "D" else False
E_answer = True if variant["answer"] == "E" else False
F_answer = True if variant["answer"] == "F" else False
G_answer = True if variant["answer"] == "G" else False
