# -*- coding: utf-8 -*-
import json
import math
import random

variants = [
    {
        "contract_term": 5,
        "planned_payback": 2,
        "long_term_asset_acquisition_v1": 10000,
        "long_term_asset_acquisition_v2": 20000,
        "interval_from": 0,
        "interval_to": 200,
        "useful_life_of_equipment_v1": 5,
        "useful_life_of_equipment_v2": 5,
        "conditionally_fixed_costs_v1": 500,
        "conditionally_fixed_costs_v2": 1000,
        "variable_costs_v1": 80,
        "variable_costs_v2": 60,
        "annual_activity_from": 100,
        "annual_activity_to": 200,
        "volume_of_production": 200,
        "interim_response": 2,
        "every_more": "every",
    },  # 1
    {
        "contract_term": 5,
        "planned_payback": 2,
        "long_term_asset_acquisition_v1": 15000,
        "long_term_asset_acquisition_v2": 20000,
        "interval_from": 201,
        "interval_to": 400,
        "useful_life_of_equipment_v1": 5,
        "useful_life_of_equipment_v2": 5,
        "conditionally_fixed_costs_v1": 750,
        "conditionally_fixed_costs_v2": 1000,
        "variable_costs_v1": 80,
        "variable_costs_v2": 60,
        "annual_activity_from": 201,
        "annual_activity_to": 400,
        "volume_of_production": 400,
        "interim_response": 2,
        "every_more": "every",
    },  # 2
    {
        "contract_term": 5,
        "planned_payback": 2,
        "long_term_asset_acquisition_v1": 20000,
        "long_term_asset_acquisition_v2": 40000,
        "interval_from": 501,
        "interval_to": 600,
        "useful_life_of_equipment_v1": 5,
        "useful_life_of_equipment_v2": 5,
        "conditionally_fixed_costs_v1": 1000,
        "conditionally_fixed_costs_v2": 2000,
        "variable_costs_v1": 80,
        "variable_costs_v2": 60,
        "annual_activity_from": 540,
        "annual_activity_to": 600,
        "volume_of_production": 600,
        "interim_response": 2,
        "every_more": "more",
    },  # 3
    {
        "contract_term": 5,
        "planned_payback": 2,
        "long_term_asset_acquisition_v1": 25000,
        "long_term_asset_acquisition_v2": 40000,
        "interval_from": 601,
        "interval_to": 800,
        "useful_life_of_equipment_v1": 5,
        "useful_life_of_equipment_v2": 5,
        "conditionally_fixed_costs_v1": 1250,
        "conditionally_fixed_costs_v2": 2000,
        "variable_costs_v1": 80,
        "variable_costs_v2": 60,
        "annual_activity_from": 700,
        "annual_activity_to": 750,
        "volume_of_production": 750,
        "interim_response": 2,
        "every_more": "every",
    },  # 4
    {
        "contract_term": 5,
        "planned_payback": 2,
        "long_term_asset_acquisition_v1": 30000,
        "long_term_asset_acquisition_v2": 40000,
        "interval_from": 801,
        "interval_to": 1000,
        "useful_life_of_equipment_v1": 5,
        "useful_life_of_equipment_v2": 5,
        "conditionally_fixed_costs_v1": 1500,
        "conditionally_fixed_costs_v2": 2000,
        "variable_costs_v1": 80,
        "variable_costs_v2": 60,
        "annual_activity_from": 900,
        "annual_activity_to": 1000,
        "volume_of_production": 1000,
        "interim_response": 2,
        "every_more": "every",
    },  # 5
    {
        "contract_term": 4,
        "planned_payback": 4,
        "long_term_asset_acquisition_v1": 10000,
        "long_term_asset_acquisition_v2": 20000,
        "interval_from": 0,
        "interval_to": 200,
        "useful_life_of_equipment_v1": 4,
        "useful_life_of_equipment_v2": 4,
        "conditionally_fixed_costs_v1": 500,
        "conditionally_fixed_costs_v2": 1000,
        "variable_costs_v1": 50,
        "variable_costs_v2": 40,
        "annual_activity_from": 50,
        "annual_activity_to": 150,
        "volume_of_production": 150,
        "interim_response": 4,
        "every_more": "every",
    },  # 6
    {
        "contract_term": 4,
        "planned_payback": 4,
        "long_term_asset_acquisition_v1": 15000,
        "long_term_asset_acquisition_v2": 20000,
        "interval_from": 201,
        "interval_to": 400,
        "useful_life_of_equipment_v1": 4,
        "useful_life_of_equipment_v2": 4,
        "conditionally_fixed_costs_v1": 750,
        "conditionally_fixed_costs_v2": 1000,
        "variable_costs_v1": 50,
        "variable_costs_v2": 40,
        "annual_activity_from": 201,
        "annual_activity_to": 250,
        "volume_of_production": 250,
        "interim_response": 4,
        "every_more": "every",
    },  # 7
    {
        "contract_term": 4,
        "planned_payback": 4,
        "long_term_asset_acquisition_v1": 20000,
        "long_term_asset_acquisition_v2": 40000,
        "interval_from": 501,
        "interval_to": 600,
        "useful_life_of_equipment_v1": 4,
        "useful_life_of_equipment_v2": 4,
        "conditionally_fixed_costs_v1": 1000,
        "conditionally_fixed_costs_v2": 2000,
        "variable_costs_v1": 50,
        "variable_costs_v2": 40,
        "annual_activity_from": 550,
        "annual_activity_to": 600,
        "volume_of_production": 600,
        "interim_response": 4,
        "every_more": "every",
    },  # 8
    {
        "contract_term": 4,
        "planned_payback": 4,
        "long_term_asset_acquisition_v1": 25000,
        "long_term_asset_acquisition_v2": 40000,
        "interval_from": 601,
        "interval_to": 800,
        "useful_life_of_equipment_v1": 4,
        "useful_life_of_equipment_v2": 4,
        "conditionally_fixed_costs_v1": 1250,
        "conditionally_fixed_costs_v2": 2000,
        "variable_costs_v1": 50,
        "variable_costs_v2": 40,
        "annual_activity_from": 700,
        "annual_activity_to": 800,
        "volume_of_production": 800,
        "interim_response": 4,
        "every_more": "every",
    },  # 9
    {
        "contract_term": 4,
        "planned_payback": 4,
        "long_term_asset_acquisition_v1": 30000,
        "long_term_asset_acquisition_v2": 40000,
        "interval_from": 801,
        "interval_to": 1000,
        "useful_life_of_equipment_v1": 4,
        "useful_life_of_equipment_v2": 4,
        "conditionally_fixed_costs_v1": 1500,
        "conditionally_fixed_costs_v2": 2000,
        "variable_costs_v1": 50,
        "variable_costs_v2": 40,
        "annual_activity_from": 850,
        "annual_activity_to": 900,
        "volume_of_production": 900,
        "interim_response": 4,
        "every_more": "every",
    },  # 10
    {
        "contract_term": 10,
        "planned_payback": 5,
        "long_term_asset_acquisition_v1": 5000,
        "long_term_asset_acquisition_v2": 9000,
        "interval_from": 0,
        "interval_to": 200,
        "useful_life_of_equipment_v1": 10,
        "useful_life_of_equipment_v2": 10,
        "conditionally_fixed_costs_v1": 250,
        "conditionally_fixed_costs_v2": 450,
        "variable_costs_v1": 90,
        "variable_costs_v2": 85,
        "annual_activity_from": 100,
        "annual_activity_to": 200,
        "volume_of_production": 200,
        "interim_response": 5,
        "every_more": "every",
    },  # 11
    {
        "contract_term": 10,
        "planned_payback": 5,
        "long_term_asset_acquisition_v1": 10000,
        "long_term_asset_acquisition_v2": 18000,
        "interval_from": 301,
        "interval_to": 400,
        "useful_life_of_equipment_v1": 10,
        "useful_life_of_equipment_v2": 10,
        "conditionally_fixed_costs_v1": 500,
        "conditionally_fixed_costs_v2": 900,
        "variable_costs_v1": 90,
        "variable_costs_v2": 85,
        "annual_activity_from": 350,
        "annual_activity_to": 400,
        "volume_of_production": 400,
        "interim_response": 5,
        "every_more": "every",
    },  # 12
    {
        "contract_term": 10,
        "planned_payback": 5,
        "long_term_asset_acquisition_v1": 15000,
        "long_term_asset_acquisition_v2": 18000,
        "interval_from": 401,
        "interval_to": 600,
        "useful_life_of_equipment_v1": 10,
        "useful_life_of_equipment_v2": 10,
        "conditionally_fixed_costs_v1": 750,
        "conditionally_fixed_costs_v2": 900,
        "variable_costs_v1": 90,
        "variable_costs_v2": 85,
        "annual_activity_from": 401,
        "annual_activity_to": 500,
        "volume_of_production": 500,
        "interim_response": 5,
        "every_more": "every",
    },  # 13
    {
        "contract_term": 10,
        "planned_payback": 5,
        "long_term_asset_acquisition_v1": 20000,
        "long_term_asset_acquisition_v2": 27000,
        "interval_from": 601,
        "interval_to": 800,
        "useful_life_of_equipment_v1": 10,
        "useful_life_of_equipment_v2": 10,
        "conditionally_fixed_costs_v1": 1000,
        "conditionally_fixed_costs_v2": 1350,
        "variable_costs_v1": 90,
        "variable_costs_v2": 85,
        "annual_activity_from": 700,
        "annual_activity_to": 800,
        "volume_of_production": 800,
        "interim_response": 5,
        "every_more": "every",
    },  # 14
    {
        "contract_term": 10,
        "planned_payback": 5,
        "long_term_asset_acquisition_v1": 25000,
        "long_term_asset_acquisition_v2": 27000,
        "interval_from": 801,
        "interval_to": 900,
        "useful_life_of_equipment_v1": 10,
        "useful_life_of_equipment_v2": 10,
        "conditionally_fixed_costs_v1": 1250,
        "conditionally_fixed_costs_v2": 1350,
        "variable_costs_v1": 90,
        "variable_costs_v2": 85,
        "annual_activity_from": 850,
        "annual_activity_to": 900,
        "volume_of_production": 900,
        "interim_response": 5,
        "every_more": "every",
    },  # 15
    {
        "contract_term": 7,
        "planned_payback": 4,
        "long_term_asset_acquisition_v1": 5000,
        "long_term_asset_acquisition_v2": 10000,
        "interval_from": 0,
        "interval_to": 200,
        "useful_life_of_equipment_v1": 7,
        "useful_life_of_equipment_v2": 7,
        "conditionally_fixed_costs_v1": 250,
        "conditionally_fixed_costs_v2": 500,
        "variable_costs_v1": 90,
        "variable_costs_v2": 87,
        "annual_activity_from": 50,
        "annual_activity_to": 150,
        "volume_of_production": 150,
        "interim_response": 4,
        "every_more": "every",
    },  # 16
    {
        "contract_term": 7,
        "planned_payback": 4,
        "long_term_asset_acquisition_v1": 10000,
        "long_term_asset_acquisition_v2": 20000,
        "interval_from": 301,
        "interval_to": 400,
        "useful_life_of_equipment_v1": 7,
        "useful_life_of_equipment_v2": 7,
        "conditionally_fixed_costs_v1": 500,
        "conditionally_fixed_costs_v2": 1000,
        "variable_costs_v1": 90,
        "variable_costs_v2": 87,
        "annual_activity_from": 301,
        "annual_activity_to": 350,
        "volume_of_production": 350,
        "interim_response": 4,
        "every_more": "every",
    },  # 17
    {
        "contract_term": 7,
        "planned_payback": 4,
        "long_term_asset_acquisition_v1": 15000,
        "long_term_asset_acquisition_v2": 20000,
        "interval_from": 401,
        "interval_to": 600,
        "useful_life_of_equipment_v1": 7,
        "useful_life_of_equipment_v2": 7,
        "conditionally_fixed_costs_v1": 750,
        "conditionally_fixed_costs_v2": 1000,
        "variable_costs_v1": 90,
        "variable_costs_v2": 87,
        "annual_activity_from": 501,
        "annual_activity_to": 600,
        "volume_of_production": 600,
        "interim_response": 4,
        "every_more": "every",
    },  # 18
    {
        "contract_term": 7,
        "planned_payback": 4,
        "long_term_asset_acquisition_v1": 20000,
        "long_term_asset_acquisition_v2": 30000,
        "interval_from": 601,
        "interval_to": 800,
        "useful_life_of_equipment_v1": 7,
        "useful_life_of_equipment_v2": 7,
        "conditionally_fixed_costs_v1": 1000,
        "conditionally_fixed_costs_v2": 1500,
        "variable_costs_v1": 90,
        "variable_costs_v2": 87,
        "annual_activity_from": 700,
        "annual_activity_to": 750,
        "volume_of_production": 750,
        "interim_response": 4,
        "every_more": "every",
    },  # 19
    {
        "contract_term": 7,
        "planned_payback": 4,
        "long_term_asset_acquisition_v1": 25000,
        "long_term_asset_acquisition_v2": 30000,
        "interval_from": 801,
        "interval_to": 900,
        "useful_life_of_equipment_v1": 7,
        "useful_life_of_equipment_v2": 7,
        "conditionally_fixed_costs_v1": 1250,
        "conditionally_fixed_costs_v2": 1500,
        "variable_costs_v1": 90,
        "variable_costs_v2": 87,
        "annual_activity_from": 801,
        "annual_activity_to": 850,
        "volume_of_production": 850,
        "interim_response": 4,
        "every_more": "every",
    },  # 20
]

# coefficient = round(random.randint(10, 99) * 0.1, 1)
coefficient = 1

variant = random.choice(variants)
variant = variants[4]

contract_term = variant["contract_term"]
planned_payback = variant["planned_payback"]
long_term_asset_acquisition_v1 = variant["long_term_asset_acquisition_v1"] * coefficient
long_term_asset_acquisition_v2 = variant["long_term_asset_acquisition_v2"] * coefficient
interval_from = variant["interval_from"]
interval_to = variant["interval_to"]
useful_life_of_equipment_v1 = variant["useful_life_of_equipment_v1"]
useful_life_of_equipment_v2 = variant["useful_life_of_equipment_v2"]
conditionally_fixed_costs_v1 = variant["conditionally_fixed_costs_v1"] * coefficient
conditionally_fixed_costs_v2 = variant["conditionally_fixed_costs_v2"] * coefficient
variable_costs_v1 = variant["variable_costs_v1"] * coefficient
variable_costs_v2 = variant["variable_costs_v2"] * coefficient
annual_activity_from = variant["annual_activity_from"]
annual_activity_to = variant["annual_activity_to"]
volume_of_production = variant["volume_of_production"]
interim_response = variant["interim_response"]
every_more = variant["every_more"]

p_z_v1 = (1/planned_payback) * long_term_asset_acquisition_v1 + conditionally_fixed_costs_v1 + (variable_costs_v1 * volume_of_production)
p_z_v2 = (1/planned_payback) * long_term_asset_acquisition_v2 + conditionally_fixed_costs_v2 + (variable_costs_v2 * volume_of_production)

gr = math.ceil((((conditionally_fixed_costs_v2-conditionally_fixed_costs_v1) + (1/planned_payback) * (long_term_asset_acquisition_v2 - long_term_asset_acquisition_v1))/(variable_costs_v1-variable_costs_v2)))

if p_z_v2 >= p_z_v1:
    recommend = "variant_1"
    option_recommend_1 = True
    option_recommend_2 = False
else:
    recommend = "variant_2"
    option_recommend_1 = False
    option_recommend_2 = True

if every_more == "every":
    option_every_more_1 = True
    option_every_more_2 = False
else:
    option_every_more_1 = False
    option_every_more_2 = True

print("Приведенные затраты (Зпр) В1", p_z_v1)

print("Приведенные затраты (Зпр) В2", p_z_v2)

print("Граница целесообразности", gr)

print("ля внедрения рекомендую вариант", recommend)
#
# print(option_recommend_1)
# print(option_recommend_2)