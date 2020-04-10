import pandas as pd
from openpyxl import Workbook
# from helpers.helpers import *
from Шульгин.helpers.helpers import get_leader_id, get_leader_id_progress

df = pd.read_excel('завершившие.xlsx')

lol = 0
for index, row in df.iterrows():
    user_p = get_leader_id_progress(row['Username'])
    if user_p != 100:
        lol += 1
        # print(index)
        print(row['Username'], " ", get_leader_id(row['Username']), user_p)

print(lol)

# print(get_leader_id_progress('Svet-lana'))