import pandas as pd
from openpyxl import Workbook
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


# wb = Workbook()
# ws = wb.active
# ws['A1'] = 'Username'
# ws['B1'] = questions[0]
# ws['C1'] = questions[1]
# ws['D1'] = questions[2]
# ws['E1'] = questions[3]
# ws['F1'] = 'leader_id'
#
#
# for index, l in enumerate(new_answers.keys()):
#     ws['A'+str(index+2)] = l
#     ws['B'+str(index+2)] = new_answers[l][questions[0]]
#     ws['C'+str(index+2)] = new_answers[l][questions[1]]
#     ws['D'+str(index+2)] = new_answers[l][questions[2]]
#     ws['E'+str(index+2)] = new_answers[l][questions[3]]
#     ws['F'+str(index+2)] = get_leader_id(l)
#
#
# wb.save("reflection_2035.xlsx")

# -------------------------------------------------------

df_1 = pd.read_excel('завершившие.xlsx')

for index, row in df_1.iterrows():
    if row['Username'] not in new_answers.keys():
        print(row['Username'])
    # user_p = get_leader_id_progress(row['Username'])
    # if user_p != 100:
    #     lol += 1
    #     # print(index)
    #     print(row['Username'], " ", get_leader_id(row['Username']), user_p)

# print(lol)