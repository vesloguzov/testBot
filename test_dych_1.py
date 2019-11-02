import json
import random
variants = [
{
    "item_1": "Законы движения планет",
    "item_2": "Кеплер"
},
{
    "item_1": "Гелиоцентрическая система мира",
    "item_2": "Коперник"
},
{
    "item_1": "Эволюционная теория",
    "item_2": "Дарвин"
},
{
    "item_1": "Основатель экспериментального метода",
    "item_2": "Галилей"
},
{
    "item_1": "Открытие радиоактивности",
    "item_2": "Беккерель"
}
]


variant_nums = random.sample(list(range(0, len(variants))), 2)

print(variant_nums)

a_1 = variants[variant_nums[0]]["item_1"]
a_2 = variants[variant_nums[1]]["item_1"]
b_1 = variants[variant_nums[0]]["item_2"]
b_2 = variants[variant_nums[1]]["item_2"]

answers = [b_1, b_2]

for index, v in enumerate(variants):
    if not index in variant_nums:
        answers.append(variants[index]["item_2"])

g_text_0 = answers[0]
g_text_1 = answers[1]
g_text_2 = answers[2]
g_text_3 = answers[3]
g_text_4 = answers[4]

print(a_1, a_2)
print(b_1, b_2)
# exclude_selected = variants[(variant_num+1):(len(variants))] + variants[:variant_num]
# items = [x["item_2"]for x in exclude_selected]
#
# print(items[4])

