import numpy as np
import json

variants = [
    {
        "n": 15,
        "p": 5,
        "t1": 1,
        "t2": 2,
        "t3": 1,
        "t4": 3,
        "t5": 1
    },
    {
        "n": 20,
        "p": 4,
        "t1": 5,
        "t2": 3,
        "t3": 4,
        "t4": 2,
        "t5": 1
    },
    {
        "n": 30,
        "p": 6,
        "t1": 2,
        "t2": 3,
        "t3": 2,
        "t4": 5,
        "t5": 3
    },
    {
        "n": 40,
        "p": 10,
        "t1": 1,
        "t2": 4,
        "t3": 3,
        "t4": 2,
        "t5": 3
    },
    {
        "n": 25,
        "p": 5,
        "t1": 3,
        "t2": 2,
        "t3": 3,
        "t4": 2,
        "t5": 3
    },
    {
        "n": 35,
        "p": 7,
        "t1": 0.5,
        "t2": 4,
        "t3": 0.5,
        "t4": 4,
        "t5": 1
    },
    {
        "n": 45,
        "p": 9,
        "t1": 1,
        "t2": 2,
        "t3": 0.5,
        "t4": 2,
        "t5": 1
    },
    {
        "n": 50,
        "p": 10,
        "t1": 2,
        "t2": 3,
        "t3": 2,
        "t4": 4,
        "t5": 1
    },
    {
        "n": 30,
        "p": 10,
        "t1": 4,
        "t2": 3,
        "t3": 2,
        "t4": 4,
        "t5": 2
    },
    {
        "n": 10,
        "p": 2,
        "t1": 3,
        "t2": 2,
        "t3": 4,
        "t4": 6,
        "t5": 2
    }
]

user_data = variants[1]

n = user_data["n"]
p = user_data["p"]
t1 = user_data["t1"]
t2 = user_data["t2"]
t3 = user_data["t3"]
t4 = user_data["t4"]
t5 = user_data["t5"]

groups_len = int(n/p)

t_list = [t1, t2, t3, t4, t5]

t = len(t_list)


if any(x - int(x) for x in t_list):
    t_list[:] = [int(x * 2) for x in t_list]
print("groups_len: ", groups_len)
print("t: ", t)
cells_1_max = int(sum(t_list))
print("cells_1_max: ", cells_1_max)
# filling table 1
cells_1_correct = np.zeros(t * cells_1_max).reshape(t, cells_1_max)
for i in list(range(0, t)):
    for j in range(0, t_list[i]):
        cells_1_correct[i][j + sum(t_list[:int(i)])] = 1

# filling table 2
cells_2_correct = np.zeros(t * (cells_1_max + max(t_list) * 2)).reshape(t, (cells_1_max + max(t_list) * 2))

print(max(t_list))
# print(cells_1_max + max(t_list) +  )

print(cells_2_correct)
for i in list(range(0, t)):
    for j in range(0, t_list[i]):
        cells_2_correct[i][j + sum(t_list[:int(i)])] = 1
        cells_2_correct[i][j + sum(t_list[:int(i)]) + max(t_list)] = 2
        cells_2_correct[i][j + sum(t_list[:int(i)]) + 2 * max(t_list)] = 3
print("--------------------------------------------------------------------------------------")

print(cells_2_correct)
# filling table 3
# cells_3_correct = np.zeros(t * (cells_1_max + max(t_list) * 4)).reshape(t, (cells_1_max + max(t_list) * 4))
# for i in list(range(0, t)):
#     for j in range(0, t_list[i]):
#         cells_3_correct[i][j] = 1
#         cells_3_correct[i][j + t_list[i]] = 2
#         cells_3_correct[i][j + t_list[i] * 2] = 3
#
# for row_num in list(range(1, t)):
#     roll_candidates = []
#     for g in list(range(1, groups_len + 1)):
#         previous_indexes = np.where(cells_3_correct[row_num - 1] == g)[0]
#         current_indexes = np.where(cells_3_correct[row_num] == g)[0]
#         if previous_indexes[-1] >= current_indexes[0]:
#             roll_candidates.append((previous_indexes[-1] - current_indexes[0]) + 1)
#     roll = 0
#     if len(roll_candidates):
#         roll = max(roll_candidates)
#         cells_3_correct[row_num] = np.roll(cells_3_correct[row_num], roll)
#
# tmp_cells_3_correct = np.transpose(cells_3_correct)
# tmp_cells_3_correct = tmp_cells_3_correct[~(tmp_cells_3_correct == 0).all(1)]
# cells_3_correct = np.transpose(tmp_cells_3_correct)
#
# cells_1_len = len(cells_1_correct[0])
# cells_2_len = len(cells_2_correct[0])
# cells_3_len = len(cells_3_correct[0])

# print(cells_1_correct)
# print(cells_2_correct)
# print(cells_3_correct)

# print(cells_1_len, 800/cells_1_len)
# print(cells_2_len, 800/cells_2_len)
# print(cells_3_len, 800/cells_3_len)

# student_data = {
#     "n": n,
#     "p": p,
#     "t1": t1,
#     "t2": t2,
#     "t3": t3,
#     "t4": t4,
#     "t5": t5,
#     "tables_len": [cells_1_len, cells_2_len, cells_3_len]
# }
#
# student_data_json = json.dumps(student_data, ensure_ascii=False).replace("\"", "'")
# # print(student_data_json)
#
# def check_answer(exp, ans):
#     student_answer = json.loads(ans)["answer"]
#     max_grade = 3
#     student_correctness = {
#         'table_1': False,
#         'table_2': False,
#         'table_3': False
#     }
#     grade = 0
#
#     if cells_1_correct.tolist() == student_answer['table_1']:
#         grade += 1
#         student_correctness['table_1'] = True
#     if cells_2_correct.tolist() == student_answer['table_2']:
#         grade += 1
#         student_correctness['table_2'] = True
#     if cells_3_correct.tolist() == student_answer['table_3']:
#         grade += 1
#         student_correctness['table_3'] = True
#
#     result_grade = grade / max_grade
#     msg = json.dumps(student_correctness)
#     if result_grade == 1:
#         return {'input_list': [{'ok': True, 'msg': msg, 'grade_decimal': 1}]}
#     elif result_grade == 0:
#         return {'input_list': [{'ok': False, 'msg': msg, 'grade_decimal': 0}]}
#     else:
#         return {'input_list': [{'ok': 'Partial', 'msg': msg, 'grade_decimal': result_grade}]}
#
#
# student_str = '{"answer":{"table_1":[[1,0,0,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,1,1,0],[0,0,0,0,0,0,0,1]],"table_2":[[1,0,0,2,0,0,3,0,0,0,0,0,0,0],[0,1,1,0,2,2,0,3,3,0,0,0,0,0],[0,0,0,1,0,0,2,0,0,3,0,0,0,0],[0,0,0,0,1,1,1,2,2,2,3,3,3,0],[0,0,0,0,0,0,0,1,0,0,2,0,0,3]],"table_3":[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]}}'

# print(check_answer(1, student_str))