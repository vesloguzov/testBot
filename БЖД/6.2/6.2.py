# -*- coding: utf-8 -*-
import random

variants = [{"floor_type": "деревянный", "humidity": "60-70", "dust": True, "temperature": "36-40", "chemically_active": False, "touch": False, "answer": 3}, {"floor_type": "кафель", "humidity": "100", "dust": False, "temperature": "20-30", "chemically_active": False, "touch": False, "answer": 3}, {"floor_type": "деревянный", "humidity": "50-70", "dust": False, "temperature": "20-30", "chemically_active": False, "touch": False, "answer": 1}, {"floor_type": "цемент", "humidity": "50-70", "dust": True, "temperature": "20-30", "chemically_active": False, "touch": False, "answer": 3}, {"floor_type": "деревянный", "humidity": "50-70", "dust": True, "temperature": "20-30", "chemically_active": False, "touch": False, "answer": 2}, {"floor_type": "бетонный", "humidity": "40-60", "dust": False, "temperature": "20-30", "chemically_active": False, "touch": True, "answer": 3}, {"floor_type": "кафель", "humidity": "40-60", "dust": False, "temperature": "20-30", "chemically_active": True, "touch": False, "answer": 3}, {"floor_type": "деревянный", "humidity": "50-70", "dust": False, "temperature": "20-30", "chemically_active": False, "touch": False, "answer": 1}, {"floor_type": "кафель", "humidity": "76-80", "dust": False, "temperature": "20-30", "chemically_active": False, "touch": False, "answer": 3}, {"floor_type": "бетонный", "humidity": "40-60", "dust": False, "temperature": "20-30", "chemically_active": False, "touch": False, "answer": 2}, {"floor_type": "кафель", "humidity": "100", "dust": False, "temperature": "36-42", "chemically_active": False, "touch": False, "answer": 3}, {"floor_type": "цемент", "humidity": "50-70", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": False, "answer": 2}, {"floor_type": "деревянный", "humidity": "50-70", "dust": True, "temperature": "36-40", "chemically_active": False, "touch": False, "answer": 3}, {"floor_type": "кафель", "humidity": "100", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": False, "answer": 3}, {"floor_type": "деревянный", "humidity": "50-70", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": False, "answer": 1}, {"floor_type": "цемент", "humidity": "50-70", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": True, "answer": 3}, {"floor_type": "деревянный", "humidity": "50-70", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": False, "answer": 1}, {"floor_type": "бетонный", "humidity": "40-60", "dust": True, "temperature": "20-35", "chemically_active": False, "touch": True, "answer": 3}, {"floor_type": "кафель", "humidity": "40-60", "dust": False, "temperature": "20-35", "chemically_active": True, "touch": False, "answer": 3}, {"floor_type": "деревянный", "humidity": "40-60", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": False, "answer": 1}, {"floor_type": "кафель", "humidity": "40-60", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": False, "answer": 2}, {"floor_type": "бетонный", "humidity": "40-60", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": False, "answer": 2}, {"floor_type": "кафель", "humidity": "40-60", "dust": False, "temperature": "36-45", "chemically_active": False, "touch": False, "answer": 3}, {"floor_type": "цемент", "humidity": "50-75", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": False, "answer": 2}, {"floor_type": "деревянный", "humidity": "50-75", "dust": True, "temperature": "36-45", "chemically_active": False, "touch": False, "answer": 3}, {"floor_type": "кафель", "humidity": "100", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": False, "answer": 3}, {"floor_type": "деревянный", "humidity": "50-75", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": False, "answer": 1}, {"floor_type": "цемент", "humidity": "50-75", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": True, "answer": 3}, {"floor_type": "деревянный", "humidity": "50-75", "dust": False, "temperature": "20-35", "chemically_active": False, "touch": False, "answer": 1}, {"floor_type": "бетонный", "humidity": "40-60", "dust": False, "temperature": "36-45", "chemically_active": False, "touch": False, "answer": 3}]

variant = random.choice(variants)

floor_type = variant['floor_type']
humidity = variant['humidity']
dust = variant['dust']
temperature = variant['temperature']
chemically_active = variant['chemically_active']
touch = variant['touch']
answer = variant['answer']

have = 'имеется'
nohave = 'нет'

dust_template = have if dust else nohave
chemically_active_template = have if chemically_active else nohave
touch_template = have if touch else nohave

class_1 = False
class_2 = False
class_3 = False

if answer == 1:
    class_1 = True
elif answer == 2:
    class_2 = True
else:
    class_3 = True

print(class_1)
print(class_2)
print(class_3)