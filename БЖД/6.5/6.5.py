import random

variants = [{
    "title": u"надзор за соблюдением трудового законодательства и иных нормативных правовых актов, содержащих нормы трудового права",
    "answer": "B"},
    {"title": u"контроль и надзор в сфере промышленной безопасности", "answer": "A"},
    {"title": u"контроль и надзор в сфере промышленной безопасности", "answer": "E"}]

variant = variants[0]

title = variant["title"]

A_answer = False
B_answer = False
C_answer = False
D_answer = False
E_answer = False
F_answer = False

if variant["answer"] == "B":
    B_answer = True
elif variant["answer"] == "A":
    A_answer = True
else:
    E_answer = True
