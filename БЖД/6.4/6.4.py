# df = pd.read_excel('6.4.xlsx', sheet_name='Sheet1').T.to_dict().values()
# import pandas as pd

import random

variants = [{"voltage": "до 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "А1", "resistance_from": 3,
             "resistance_to": 10, "answer": False},
            {"voltage": "до 1000 В", "neutral_mode": "изолированная", "network_symbol": "Б1", "resistance_from": 1,
             "resistance_to": 4, "answer": True},
            {"voltage": "выше 1000 В", "neutral_mode": "изолированная", "network_symbol": "В", "resistance_from": 1,
             "resistance_to": 10, "answer": True},
            {"voltage": "выше 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "Г", "resistance_from": 1,
             "resistance_to": 5, "answer": False},
            {"voltage": "выше 1000 В", "neutral_mode": "изолированная", "network_symbol": "В", "resistance_from": 1,
             "resistance_to": 10, "answer": True},
            {"voltage": "до 1000 В", "neutral_mode": "изолированная", "network_symbol": "Б2", "resistance_from": 1,
             "resistance_to": 10, "answer": True},
            {"voltage": "выше 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "Г",
             "resistance_from": 0.1, "resistance_to": 0.5, "answer": True},
            {"voltage": "выше 1000 В", "neutral_mode": "изолированная", "network_symbol": "В", "resistance_from": 11,
             "resistance_to": 15, "answer": False},
            {"voltage": "до 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "А2", "resistance_from": 1,
             "resistance_to": 4, "answer": True},
            {"voltage": "выше 1000 В", "neutral_mode": "изолированная", "network_symbol": "Б1", "resistance_from": 5,
             "resistance_to": 10, "answer": False},
            {"voltage": "выше 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "Г", "resistance_from": 1,
             "resistance_to": 5, "answer": False},
            {"voltage": "выше 1000 В", "neutral_mode": "изолированная", "network_symbol": "В", "resistance_from": 1,
             "resistance_to": 10, "answer": True},
            {"voltage": "до 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "А3", "resistance_from": 1,
             "resistance_to": 8, "answer": True},
            {"voltage": "до 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "А1", "resistance_from": 5,
             "resistance_to": 10, "answer": False},
            {"voltage": "выше 1000 В", "neutral_mode": "изолированная", "network_symbol": "В", "resistance_from": 1,
             "resistance_to": 10, "answer": True},
            {"voltage": "выше 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "Г", "resistance_from": 1,
             "resistance_to": 5, "answer": False},
            {"voltage": "до 1000 В", "neutral_mode": "изолированная", "network_symbol": "Б1", "resistance_from": 1,
             "resistance_to": 4, "answer": True},
            {"voltage": "выше 1000 В", "neutral_mode": "изолированная", "network_symbol": "В", "resistance_from": 1,
             "resistance_to": 10, "answer": True},
            {"voltage": "выше 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "Г", "resistance_from": 1,
             "resistance_to": 5, "answer": False},
            {"voltage": "выше 1000 В", "neutral_mode": "изолированная", "network_symbol": "В", "resistance_from": 11,
             "resistance_to": 15, "answer": False},
            {"voltage": "до 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "А1", "resistance_from": 5,
             "resistance_to": 10, "answer": False},
            {"voltage": "до 1000 В", "neutral_mode": "изолированная", "network_symbol": "Б1", "resistance_from": 1,
             "resistance_to": 4, "answer": True},
            {"voltage": "до 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "А2", "resistance_from": 5,
             "resistance_to": 10, "answer": False},
            {"voltage": "до 1000 В", "neutral_mode": "изолированная", "network_symbol": "Б2", "resistance_from": 1,
             "resistance_to": 10, "answer": True},
            {"voltage": "до 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "А3", "resistance_from": 1,
             "resistance_to": 8, "answer": True},
            {"voltage": "выше 1000 В", "neutral_mode": "изолированная", "network_symbol": "В", "resistance_from": 1,
             "resistance_to": 10, "answer": True},
            {"voltage": "до 1000 В", "neutral_mode": "изолированная", "network_symbol": "Б1", "resistance_from": 1,
             "resistance_to": 4, "answer": True},
            {"voltage": "до 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "А1", "resistance_from": 3,
             "resistance_to": 8, "answer": False},
            {"voltage": "до 1000 В", "neutral_mode": "изолированная", "network_symbol": "Б2", "resistance_from": 11,
             "resistance_to": 15, "answer": False},
            {"voltage": "выше 1000 В", "neutral_mode": "глухозаземленная", "network_symbol": "Г", "resistance_to": 1,
             "resistance_to": 5, "answer": False}]

variant = random.choice(variants)

if variant["resistance_from"] >= 1:
    resistance = random.randrange(variant["resistance_from"], variant["resistance_to"] + 1, 1)
else:
    resistance = random.randrange(variant["resistance_from"]*10, (variant["resistance_to"]*10) + 1, 1)/10

if variant['answer']:
    answer_1 = True
    answer_2 = False
else:
    answer_1 = False
    answer_2 = True

voltage = variant['voltage']
neutral_mode = variant['neutral_mode']
network_symbol = variant['network_symbol']
