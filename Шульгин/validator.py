import pandas as pd
from openpyxl import Workbook
# from helpers.helpers import *
from Шульгин.helpers.helpers import get_leader_id, get_leader_id_progress, leader_id_progress

questions = [
    "Чему новому, как вам кажется, вы научились ?",
    "Выберите из предложенного списка то, чему вы могли научиться / научились в рамках программы:",
    "Поделитесь вашими комментариями или пожеланиями по поводу того, с чем вы познакомились?",
    "Перечислите основные этапы деятельности, в которую вы были вовлечены и благодаря которой научились чему-то"
]

df = pd.read_excel('Итог для ЦС.xlsx')

lol = 0
for index, row in df.iterrows():
    # print(row['Leader ID'])
    user_p = leader_id_progress(str(row['Leader ID']))
    # if str(row['Leader ID']) == '1053627':
    #     print(user_p, row)
    # print(str(row['Leader ID']))

    if user_p != 100:
        lol += 1
        print(row['ФИО'], row['email'], user_p)


print(lol)

# print(get_leader_id_progress('Svet-lana'))