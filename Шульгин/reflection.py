import pandas as pd
from openpyxl import Workbook

df = pd.read_excel('reflection_src.xlsx', sheet_name='Лист1')

questions = [
    "Перечислите основные этапы деятельности, в которую вы были вовлечены и благодаря которой научились чему-то",
    "Поделитесь вашими комментариями или пожеланиями по поводу того, с чем вы познакомились?",
    "Выберите из предложенного списка то, чему вы могли научиться / научились в рамках программы:",
    "Чему новому, как вам кажется, вы научились ?"
]

new_answers = {}
answers = df.to_dict('index')

test_list = []
for ind in answers.keys():
    test_list.append(answers[ind]['Username'])
    new_answers[answers[ind]['Username']] = {
        questions[0]: "",
        questions[1]: "",
        questions[2]: "",
        questions[3]: ""
    }

for ind in answers.keys():
    new_answers[answers[ind]['Username']][answers[ind]['Вопрос']] = answers[ind]['Ответ']

# lol = 0
# for l in new_answers.keys():
#     if new_answers[l][questions[0]] == "" or new_answers[l][questions[1]] == "" or new_answers[l][questions[2]] == "" or new_answers[l][questions[3]] == "":
#         lol = lol+1

wb = Workbook()
ws = wb.active
ws['A1'] = 'Username'
ws['B1'] = questions[0]
ws['C1'] = questions[1]
ws['D1'] = questions[2]
ws['E1'] = questions[3]

for index, l in enumerate(new_answers.keys()):
    ws['A'+str(index+2)] = l
    ws['B'+str(index+2)] = new_answers[l][questions[0]]
    ws['C'+str(index+2)] = new_answers[l][questions[1]]
    ws['D'+str(index+2)] = new_answers[l][questions[2]]
    ws['E'+str(index+2)] = new_answers[l][questions[3]]
    print(new_answers[l])

wb.save("reflection_2035.xlsx")
# printt()