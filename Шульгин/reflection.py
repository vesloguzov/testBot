import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font
# from helpers.helpers import *
from Шульгин.helpers.helpers import get_leader_id

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

final_list = {}
for t in new_answers.keys():
    if len(get_leader_id(t)) > 0:
        final_list[t] = new_answers[t]

wb = Workbook()
ws = wb.active
ws['A1'] = 'Leader ID'
ws['A1'].font = Font(bold=True)
ws['B1'] = 'Дата прохождения рефлексии'
ws['B1'].font = Font(bold=True)
ws['C1'] = questions[0]
ws['C1'].font = Font(bold=True)
ws['D1'] = questions[1]
ws['D1'].font = Font(bold=True)
ws['E1'] = questions[2]
ws['E1'].font = Font(bold=True)
ws['F1'] = questions[3]
ws['F1'].font = Font(bold=True)

for index, l in enumerate(final_list.keys()):
    ws['A'+str(index+2)] = get_leader_id(l)
    ws['B' + str(index + 2)] = ""
    ws['C'+str(index+2)] = new_answers[l][questions[0]]
    ws['D'+str(index+2)] = new_answers[l][questions[1]]
    ws['E'+str(index+2)] = new_answers[l][questions[2]]
    ws['F'+str(index+2)] = new_answers[l][questions[3]]
    # ws['G'+str(index+2)] = l


wb.save("reflection_2035.xlsx")

# -------------------------------------------------------

