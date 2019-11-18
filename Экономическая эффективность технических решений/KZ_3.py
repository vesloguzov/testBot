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
        "interim_response": 2
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
        "interim_response": 2
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
        "interim_response": 2
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
        "interim_response": 2
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
        "interim_response": 2
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
        "interim_response": 4
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
        "interim_response": 4
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
        "interim_response": 4
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
        "interim_response": 4
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
        "interim_response": 4
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
        "interim_response": 5
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
        "interim_response": 5
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
        "interim_response": 5
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
        "interim_response": 5
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
        "interim_response": 5
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
        "interim_response": 4
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
        "interim_response": 4
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
        "interim_response": 4
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
        "interim_response": 4
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
        "interim_response": 4
    },  # 20
]

# variant = random.choice(variants)
variant = variants[9]

K_1 = variant["long_term_asset_acquisition_v1"]
K_2 = variant["long_term_asset_acquisition_v2"]

S_post_1 = variant["conditionally_fixed_costs_v1"]
S_post_2 = variant["conditionally_fixed_costs_v2"]

S_per_ed_1 = variant["variable_costs_v1"]
S_per_ed_2 = variant["variable_costs_v2"]

N = variant["volume_of_production"]

T_okn = variant["planned_payback"]

p_z_v1 = (1/T_okn) * K_1 + S_post_1 + (S_per_ed_1 * N)
p_z_v2 = (1/T_okn) * K_2 + S_post_2 + (S_per_ed_2 * N)
gr = ((S_post_2-S_post_1) + (1/T_okn) * (K_2 - K_1))/(S_per_ed_1-S_per_ed_2)

if p_z_v1 <= p_z_v2:
    recommend = "variant_1"
else:
    recommend = "variant_2"

print("Приведенные затраты (Зпр) В1", p_z_v1)
print("Приведенные затраты (Зпр) В2", p_z_v2)
print("Граница целесообразности", gr)
print("ля внедрения рекомендую вариант", recommend)