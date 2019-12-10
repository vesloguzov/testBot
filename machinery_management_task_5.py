# -*- coding: utf-8 -*-
import json
import math

source = [[1, 3, 2, 1.5, 2, 1, 5, 2, 2, 16, 3, 11, 16, 3, 5, 22, 4, 7, 15, 4, 6, 8, 3],
          [2, 3, 2, 8, 10, 1, 6, 2, 2, 48, 3, 11, 18, 3, 5, 30, 4, 7, 19, 4, 6, 11, 3],
          [3, 3, 2, 16, 20, 1, 8, 2, 2, 80, 3, 11, 21, 3, 5, 37, 4, 7, 20, 4, 6, 16, 3],
          [4, 3, 1, 18, 22, 1, 4, 2, 2, 80, 3, 2, 19, 3, 2, 85, 3, 2, 23, 4, 2, 62, 5],
          [5, 3, 1, 21, 26, 1, 6, 2, 3, 67, 3, 2, 19, 3, 2, 90, 3, 2, 53, 4, 2, 6, 5],
          [6, 3, 1, 101, 120, 1, 7, 2, 3, 36, 3, 3, 25, 3, 3, 95, 3, 3, 123, 4, 3, 16, 5],
          [7, 3, 2, 1.6, 2, 1, 2, 2, 2, 12, 3, 2, 10, 3, 2, 9, 3, 2, 7, 3, 3, 44, 4],
          [8, 3, 2, 1.4, 2, 1, 2, 2, 2, 12, 3, 2, 11, 3, 2, 9, 3, 2, 7, 3, 3, 47, 4],
          [9, 3, 2, 2.2, 3, 1, 2, 2, 2, 13, 3, 2, 14, 3, 2, 9, 3, 2, 7, 3, 3, 50, 4],
          [10, 3, 2, 3.2, 5, 1, 3, 2, 2, 19, 3, 2, 9, 3, 2, 62, 3, 3, 12, 3, 12, 27, 4],
          [11, 3, 2, 6, 7, 1, 3, 2, 2, 20, 3, 2, 11, 3, 2, 77, 3, 3, 12, 3, 12, 47, 4],
          [12, 3, 2, 10, 12, 1, 3, 2, 2, 22, 3, 2, 12, 3, 2, 110, 3, 2, 13, 3, 12, 87, 4],
          [13, 3, 2, 1.3, 2, 1, 3, 2, 2, 14, 3, 2, 8, 3, 2, 6, 3, 2, 13, 3, 11, 69, 3],
          [14, 3, 2, 2.3, 3, 1, 3, 2, 2, 15, 3, 2, 9, 3, 2, 7, 3, 2, 14, 3, 11, 87, 3],
          [15, 3, 2, 5.5, 7, 1, 2, 2, 2, 10, 3, 2, 9, 3, 2, 12, 3, 6, 6, 3, 11, 13, 3],
          [16, 3, 2, 2.4, 3, 1, 3, 2, 2, 11, 3, 2, 11, 3, 2, 14, 3, 6, 5, 3, 11, 17, 2],
          [17, 3, 2, 20, 25, 1, 3, 3, 2, 8, 3, 2, 6, 3, 2, 7, 3, 14, 12, 3, 7, 36, 2],
          [18, 3, 2, 21, 25, 1, 4, 3, 2, 6, 3, 2, 6, 3, 2, 10, 3, 14, 14, 3, 7, 38, 2],
          [19, 1, 2, 2.2, 3, 1, 4, 3, 2, 10, 3, 2, 12, 3, 3, 10, 3, 14, 15, 3, 7, 15, 2],
          [20, 1, 3, 4.8, 6, 2, 24, 3, 2, 35, 3, 2, 25, 3, 14, 2, 2, 9, 10, 4, 10, 12, 4],
          [21, 1, 3, 1.3, 2, 1, 5, 2, 2, 56, 3, 9, 55, 4, 10, 60, 4, 14, 2, 2, 12, 10, 3],
          [22, 1, 3, 2.7, 4, 1, 6, 2, 2, 69, 3, 9, 66, 4, 10, 60, 4, 14, 2, 2, 6, 8, 3],
          [23, 3, 2, 2.1, 3, 1, 5, 2, 2, 33, 4, 2, 9, 4, 8, 55, 4, 11, 3, 4, 13, 7, 4],
          [24, 2, 4, 1.2, 2, 2, 13, 2, 2, 19, 4, 8, 21, 4, 2, 11, 4, 7, 59, 4, 3, 4, 4],
          [25, 1, 0, 22, 26, 2, 46, 3, 2, 29, 3, 2, 33, 3, 2, 69, 3, 2, 26, 3, 3, 27, 4],
          [26, 1, 0, 6, 8, 3, 15, 3, 2, 35, 3, 2, 44, 3, 2, 72, 3, 2, 42, 3, 3, 37, 4],
          [27, 3, 2, 1.4, 2, 1, 3, 2, 2, 43, 3, 2, 34, 4, 11, 51, 3, 13, 16, 3, 6, 12, 3],
          [28, 3, 2, 1.3, 2, 1, 4, 2, 2, 40, 3, 3, 41, 4, 11, 95, 3, 13, 18, 3, 6, 18, 3],
          [29, 1, 2, 105, 130, 3, 6, 2, 2, 116, 4, 3, 35, 4, 11, 32, 3, 6, 24, 3, 6, 135, 4],
          [30, 1, 2, 248, 275, 3, 6, 2, 2, 102, 4, 3, 37, 4, 11, 32, 3, 6, 34, 3, 6, 44, 4]]
for row in source:
    d = {
        "product_num": row[0],
        "blank_type": row[1],
        "material": row[2],
        "weight": row[3],
        "consumption": row[4],
        "operations": {
            "operation_1": {
                "model": row[5],
                "time": row[6],
                "rank": row[7]
            },
            "operation_2": {
                "model": row[8],
                "time": row[9],
                "rank": row[10]
            },
            "operation_3": {
                "model": row[11],
                "time": row[12],
                "rank": row[13]
            },
            "operation_4": {
                "model": row[14],
                "time": row[15],
                "rank": row[16]
            },
            "operation_5": {
                "model": row[17],
                "time": row[18],
                "rank": row[19]
            },
            "operation_6": {
                "model": row[20],
                "time": row[21],
                "rank": row[22]
            }
        }
    }
    # print(d)


products = [{"operations": {"operation_1": {"model": 1, "rank": 2, "time": 5},
                            "operation_3": {"model": 11, "rank": 3, "time": 16},
                            "operation_2": {"model": 2, "rank": 3, "time": 16},
                            "operation_5": {"model": 7, "rank": 4, "time": 15},
                            "operation_4": {"model": 5, "rank": 4, "time": 22},
                            "operation_6": {"model": 6, "rank": 3, "time": 8}},
             "product_num": 1, "weight": 1.5, "consumption": 2, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 6},
                            "operation_3": {"model": 11, "rank": 3, "time": 18},
                            "operation_2": {"model": 2, "rank": 3, "time": 48},
                            "operation_5": {"model": 7, "rank": 4, "time": 19},
                            "operation_4": {"model": 5, "rank": 4, "time": 30},
                            "operation_6": {"model": 6, "rank": 3, "time": 11}}, "product_num": 2, "weight": 8,
             "consumption": 10,
             "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 8},
                            "operation_3": {"model": 11, "rank": 3, "time": 21},
                            "operation_2": {"model": 2, "rank": 3, "time": 80},
                            "operation_5": {"model": 7, "rank": 4, "time": 20},
                            "operation_4": {"model": 5, "rank": 4, "time": 37},
                            "operation_6": {"model": 6, "rank": 3, "time": 16}}, "product_num": 3, "weight": 16,
             "consumption": 20,
             "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 4},
                            "operation_3": {"model": 2, "rank": 3, "time": 19},
                            "operation_2": {"model": 2, "rank": 3, "time": 80},
                            "operation_5": {"model": 2, "rank": 4, "time": 23},
                            "operation_4": {"model": 2, "rank": 3, "time": 85},
                            "operation_6": {"model": 2, "rank": 5, "time": 62}}, "product_num": 4, "weight": 18,
             "consumption": 22,
             "material": 1, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 6},
                            "operation_3": {"model": 2, "rank": 3, "time": 19},
                            "operation_2": {"model": 3, "rank": 3, "time": 67},
                            "operation_5": {"model": 2, "rank": 4, "time": 53},
                            "operation_4": {"model": 2, "rank": 3, "time": 90},
                            "operation_6": {"model": 2, "rank": 5, "time": 6}},
             "product_num": 5, "weight": 21, "consumption": 26, "material": 1, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 7},
                            "operation_3": {"model": 3, "rank": 3, "time": 25},
                            "operation_2": {"model": 3, "rank": 3, "time": 36},
                            "operation_5": {"model": 3, "rank": 4, "time": 123},
                            "operation_4": {"model": 3, "rank": 3, "time": 95},
                            "operation_6": {"model": 3, "rank": 5, "time": 16}}, "product_num": 6, "weight": 101,
             "consumption": 120, "material": 1, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 2},
                            "operation_3": {"model": 2, "rank": 3, "time": 10},
                            "operation_2": {"model": 2, "rank": 3, "time": 12},
                            "operation_5": {"model": 2, "rank": 3, "time": 7},
                            "operation_4": {"model": 2, "rank": 3, "time": 9},
                            "operation_6": {"model": 3, "rank": 4, "time": 44}},
             "product_num": 7, "weight": 1.6, "consumption": 2, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 2},
                            "operation_3": {"model": 2, "rank": 3, "time": 11},
                            "operation_2": {"model": 2, "rank": 3, "time": 12},
                            "operation_5": {"model": 2, "rank": 3, "time": 7},
                            "operation_4": {"model": 2, "rank": 3, "time": 9},
                            "operation_6": {"model": 3, "rank": 4, "time": 47}},
             "product_num": 8, "weight": 1.4, "consumption": 2, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 2},
                            "operation_3": {"model": 2, "rank": 3, "time": 14},
                            "operation_2": {"model": 2, "rank": 3, "time": 13},
                            "operation_5": {"model": 2, "rank": 3, "time": 7},
                            "operation_4": {"model": 2, "rank": 3, "time": 9},
                            "operation_6": {"model": 3, "rank": 4, "time": 50}},
             "product_num": 9, "weight": 2.2, "consumption": 3, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 3},
                            "operation_3": {"model": 2, "rank": 3, "time": 9},
                            "operation_2": {"model": 2, "rank": 3, "time": 19},
                            "operation_5": {"model": 3, "rank": 3, "time": 12},
                            "operation_4": {"model": 2, "rank": 3, "time": 62},
                            "operation_6": {"model": 12, "rank": 4, "time": 27}}, "product_num": 10, "weight": 3.2,
             "consumption": 5, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 3},
                            "operation_3": {"model": 2, "rank": 3, "time": 11},
                            "operation_2": {"model": 2, "rank": 3, "time": 20},
                            "operation_5": {"model": 3, "rank": 3, "time": 12},
                            "operation_4": {"model": 2, "rank": 3, "time": 77},
                            "operation_6": {"model": 12, "rank": 4, "time": 47}}, "product_num": 11, "weight": 6,
             "consumption": 7,
             "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 3},
                            "operation_3": {"model": 2, "rank": 3, "time": 12},
                            "operation_2": {"model": 2, "rank": 3, "time": 22},
                            "operation_5": {"model": 2, "rank": 3, "time": 13},
                            "operation_4": {"model": 2, "rank": 3, "time": 110},
                            "operation_6": {"model": 12, "rank": 4, "time": 87}}, "product_num": 12, "weight": 10,
             "consumption": 12, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 3},
                            "operation_3": {"model": 2, "rank": 3, "time": 8},
                            "operation_2": {"model": 2, "rank": 3, "time": 14},
                            "operation_5": {"model": 2, "rank": 3, "time": 13},
                            "operation_4": {"model": 2, "rank": 3, "time": 6},
                            "operation_6": {"model": 11, "rank": 3, "time": 69}}, "product_num": 13, "weight": 1.3,
             "consumption": 2, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 3},
                            "operation_3": {"model": 2, "rank": 3, "time": 9},
                            "operation_2": {"model": 2, "rank": 3, "time": 15},
                            "operation_5": {"model": 2, "rank": 3, "time": 14},
                            "operation_4": {"model": 2, "rank": 3, "time": 7},
                            "operation_6": {"model": 11, "rank": 3, "time": 87}}, "product_num": 14, "weight": 2.3,
             "consumption": 3, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 2},
                            "operation_3": {"model": 2, "rank": 3, "time": 9},
                            "operation_2": {"model": 2, "rank": 3, "time": 10},
                            "operation_5": {"model": 6, "rank": 3, "time": 6},
                            "operation_4": {"model": 2, "rank": 3, "time": 12},
                            "operation_6": {"model": 11, "rank": 3, "time": 13}}, "product_num": 15, "weight": 5.5,
             "consumption": 7, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 3},
                            "operation_3": {"model": 2, "rank": 3, "time": 11},
                            "operation_2": {"model": 2, "rank": 3, "time": 11},
                            "operation_5": {"model": 6, "rank": 3, "time": 5},
                            "operation_4": {"model": 2, "rank": 3, "time": 14},
                            "operation_6": {"model": 11, "rank": 2, "time": 17}}, "product_num": 16, "weight": 2.4,
             "consumption": 3, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 3, "time": 3},
                            "operation_3": {"model": 2, "rank": 3, "time": 6},
                            "operation_2": {"model": 2, "rank": 3, "time": 8},
                            "operation_5": {"model": 14, "rank": 3, "time": 12},
                            "operation_4": {"model": 2, "rank": 3, "time": 7},
                            "operation_6": {"model": 7, "rank": 2, "time": 36}},
             "product_num": 17, "weight": 20, "consumption": 25, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 3, "time": 4},
                            "operation_3": {"model": 2, "rank": 3, "time": 6},
                            "operation_2": {"model": 2, "rank": 3, "time": 6},
                            "operation_5": {"model": 14, "rank": 3, "time": 14},
                            "operation_4": {"model": 2, "rank": 3, "time": 10},
                            "operation_6": {"model": 7, "rank": 2, "time": 38}}, "product_num": 18, "weight": 21,
             "consumption": 25, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 3, "time": 4},
                            "operation_3": {"model": 2, "rank": 3, "time": 12},
                            "operation_2": {"model": 2, "rank": 3, "time": 10},
                            "operation_5": {"model": 14, "rank": 3, "time": 15},
                            "operation_4": {"model": 3, "rank": 3, "time": 10},
                            "operation_6": {"model": 7, "rank": 2, "time": 15}}, "product_num": 19, "weight": 2.2,
             "consumption": 3, "material": 2, "blank_type": 1},
            {"operations": {"operation_1": {"model": 2, "rank": 3, "time": 24},
                            "operation_3": {"model": 2, "rank": 3, "time": 25},
                            "operation_2": {"model": 2, "rank": 3, "time": 35},
                            "operation_5": {"model": 9, "rank": 4, "time": 10},
                            "operation_4": {"model": 14, "rank": 2, "time": 2},
                            "operation_6": {"model": 10, "rank": 4, "time": 12}}, "product_num": 20, "weight": 4.8,
             "consumption": 6, "material": 3, "blank_type": 1},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 5},
                            "operation_3": {"model": 9, "rank": 4, "time": 55},
                            "operation_2": {"model": 2, "rank": 3, "time": 56},
                            "operation_5": {"model": 14, "rank": 2, "time": 2},
                            "operation_4": {"model": 10, "rank": 4, "time": 60},
                            "operation_6": {"model": 12, "rank": 3, "time": 10}}, "product_num": 21, "weight": 1.3,
             "consumption": 2, "material": 3, "blank_type": 1},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 6},
                            "operation_3": {"model": 9, "rank": 4, "time": 66},
                            "operation_2": {"model": 2, "rank": 3, "time": 69},
                            "operation_5": {"model": 14, "rank": 2, "time": 2},
                            "operation_4": {"model": 10, "rank": 4, "time": 60},
                            "operation_6": {"model": 6, "rank": 3, "time": 8}}, "product_num": 22, "weight": 2.7,
             "consumption": 4,
             "material": 3, "blank_type": 1},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 5},
                            "operation_3": {"model": 2, "rank": 4, "time": 9},
                            "operation_2": {"model": 2, "rank": 4, "time": 33},
                            "operation_5": {"model": 11, "rank": 4, "time": 3},
                            "operation_4": {"model": 8, "rank": 4, "time": 55},
                            "operation_6": {"model": 13, "rank": 4, "time": 7}}, "product_num": 23, "weight": 2.1,
             "consumption": 3, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 2, "rank": 2, "time": 13},
                            "operation_3": {"model": 8, "rank": 4, "time": 21},
                            "operation_2": {"model": 2, "rank": 4, "time": 19},
                            "operation_5": {"model": 7, "rank": 4, "time": 59},
                            "operation_4": {"model": 2, "rank": 4, "time": 11},
                            "operation_6": {"model": 3, "rank": 4, "time": 4}},
             "product_num": 24, "weight": 1.2, "consumption": 2, "material": 4, "blank_type": 2},
            {"operations": {"operation_1": {"model": 2, "rank": 3, "time": 46},
                            "operation_3": {"model": 2, "rank": 3, "time": 33},
                            "operation_2": {"model": 2, "rank": 3, "time": 29},
                            "operation_5": {"model": 2, "rank": 3, "time": 26},
                            "operation_4": {"model": 2, "rank": 3, "time": 69},
                            "operation_6": {"model": 3, "rank": 4, "time": 27}}, "product_num": 25, "weight": 22,
             "consumption": 26, "material": 0, "blank_type": 1},
            {"operations": {"operation_1": {"model": 3, "rank": 3, "time": 15},
                            "operation_3": {"model": 2, "rank": 3, "time": 44},
                            "operation_2": {"model": 2, "rank": 3, "time": 35},
                            "operation_5": {"model": 2, "rank": 3, "time": 42},
                            "operation_4": {"model": 2, "rank": 3, "time": 72},
                            "operation_6": {"model": 3, "rank": 4, "time": 37}}, "product_num": 26, "weight": 6,
             "consumption": 8,
             "material": 0, "blank_type": 1},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 3},
                            "operation_3": {"model": 2, "rank": 4, "time": 34},
                            "operation_2": {"model": 2, "rank": 3, "time": 43},
                            "operation_5": {"model": 13, "rank": 3, "time": 16},
                            "operation_4": {"model": 11, "rank": 3, "time": 51},
                            "operation_6": {"model": 6, "rank": 3, "time": 12}}, "product_num": 27, "weight": 1.4,
             "consumption": 2, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 1, "rank": 2, "time": 4},
                            "operation_3": {"model": 3, "rank": 4, "time": 41},
                            "operation_2": {"model": 2, "rank": 3, "time": 40},
                            "operation_5": {"model": 13, "rank": 3, "time": 18},
                            "operation_4": {"model": 11, "rank": 3, "time": 95},
                            "operation_6": {"model": 6, "rank": 3, "time": 18}}, "product_num": 28, "weight": 1.3,
             "consumption": 2, "material": 2, "blank_type": 3},
            {"operations": {"operation_1": {"model": 3, "rank": 2, "time": 6},
                            "operation_3": {"model": 3, "rank": 4, "time": 35},
                            "operation_2": {"model": 2, "rank": 4, "time": 116},
                            "operation_5": {"model": 6, "rank": 3, "time": 24},
                            "operation_4": {"model": 11, "rank": 3, "time": 32},
                            "operation_6": {"model": 6, "rank": 4, "time": 135}}, "product_num": 29, "weight": 105,
             "consumption": 130, "material": 2, "blank_type": 1},
            {"operations": {"operation_1": {"model": 3, "rank": 2, "time": 6},
                            "operation_3": {"model": 3, "rank": 4, "time": 37},
                            "operation_2": {"model": 2, "rank": 4, "time": 102},
                            "operation_5": {"model": 6, "rank": 3, "time": 34},
                            "operation_4": {"model": 11, "rank": 3, "time": 32},
                            "operation_6": {"model": 6, "rank": 4, "time": 44}}, "product_num": 30, "weight": 248,
             "consumption": 275, "material": 2, "blank_type": 1}
]

# Резчик carver
# Токарь turner
# Шлифовщик grinder
# Фрезеровщик milling
# Долбёжник mortar
# Протяжчик broach



employees = {
    "carver": {
        "title": "Резчик",
        "id": "carver",
        "title_ru": "Rezchik"
    },
    "turner": {
        "title": "Токарь",
        "id": "turner",
        "title_ru": "Tokar'"
    },
    "grinder": {
        "title": "Шлифовщик",
        "id": "grinder",
        "title_ru": "Schlifovschik"
    },
    "milling": {
        "title": "Фрезеровщик",
        "id": "milling",
        "title_ru": "Frezerovschik"
    },
    "mortar": {
        "title": "Долбёжник",
        "id": "mortar",
        "title_ru": "Dolbezhnik"
    },
    "broach": {
        "title": "Протяжчик",
        "id": "broach",
        "title_ru": "Protyazhchik"
    }
}

equipment = [
    {'equipment_title': u'Отрезная пила', 'equipment_num': 1, 'profession': 'carver', 'equipment_model': '8642'},
    {'equipment_title': u'Токарно-винторезный станок', 'equipment_num': 2, 'profession': 'turner',
     'equipment_model': '1610'},
    {'equipment_title': u'Токарно-винторезный станок', 'equipment_num': 3, 'profession': 'turner',
     'equipment_model': '165'},
    {'equipment_title': u'Шлице-шлифовальный станок', 'equipment_num': 4, 'profession': 'grinder',
     'equipment_model': '3451B'},
    {'equipment_title': u'Круглошлифовальный станок', 'equipment_num': 5, 'profession': 'grinder',
     'equipment_model': '3M123'},
    {'equipment_title': u'Круглошлифовальный станок', 'equipment_num': 6, 'profession': 'grinder',
     'equipment_model': '3A161'},
    {'equipment_title': u'Зубофрезерный станок', 'equipment_num': 7, 'profession': 'milling',
     'equipment_model': '5A312'},
    {'equipment_title': u'Зубофрезерный станок', 'equipment_num': 8, 'profession': 'milling', 'equipment_model': 'E311'},
    {'equipment_title': u'Зубодолбежный полуавтомат', 'equipment_num': 9, 'profession': 'mortar',
     'equipment_model': '5140'},
    {'equipment_title': u'Зубозакругляющий станок', 'equipment_num': 10, 'profession': 'milling',
     'equipment_model': '5580'},
    {'equipment_title': u'Горизонтально-фрезерный станок', 'equipment_num': 11, 'profession': 'milling',
     'equipment_model': '6M80'},
    {'equipment_title': u'Вертикально-фрезерный станок', 'equipment_num': 12, 'profession': 'milling',
     'equipment_model': '6H10'},
    {'equipment_title': u'Долбежный станок', 'equipment_num': 13, 'profession': 'mortar', 'equipment_model': '7A420'},
    {'equipment_title': u'Горизонтально-протяжный станок', 'equipment_num': 14, 'profession': 'broach',
     'equipment_model': '7B510'}]

def get_product(num):
    l = list(filter(lambda x: x["product_num"] == num, products))
    if len(l) > 0:
        return l[0]
    else:
        return None


def get_equipment(num):
    l = list(filter(lambda x: x["equipment_num"] == num, equipment))
    if len(l) > 0:
        return l[0]
    else:
        return None


manufactured_products = []


# часов в смене
emp_hours = 8
equ_hours = 8

# смен в дне
emp_workdays = 1
equ_workdays = 2

# дней в месяце
emp_days = 21
equ_days = 20

# месяцев в году
emp_month = 11
equ_month = 12

# часов в году
emp_year_h = 1848
equ_year_h = 3840

load_coeff = 0.85
load_coeff_display = int(load_coeff * 100)

time_coeff = 1.1

# manufactured_products = [1, 2, 30]

products_1_count = 40000
products_2_count = 20000
products_3_count = 30000


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list




# used_equipment = []
# used_employees = []



# for m_p_num in manufactured_products:
#     for operation in get_product(m_p_num)["operations"]:
#         op = get_product(m_p_num)["operations"][operation]
#         used_equipment.append(op["model"])
#         used_employees.append({"profession": get_equipment(op["model"])["profession"], "rank": op["rank"]})
#
# used_equipment = sorted(unique(used_equipment))
# used_equipment_count = len(used_equipment)
#
# used_employees = unique(used_employees)
# used_employees_count = len(used_employees)
#
# table_1 = []
# for u_e in used_equipment:
#     str_u_e = {"equipment_num": u_e, "times": []}
#     for product in manufactured_products:
#         sum_time = 0
#         current_product = get_product(product)
#         for op in current_product["operations"]:
#             if current_product["operations"][op]["model"] == u_e:
#                 sum_time += current_product["operations"][op]["time"]
#         str_u_e["times"].append(sum_time)
#     table_1.append(str_u_e)
#
# table_2 = []
# for e_u in table_1:
#     str_u_e = {"equipment_num": e_u["equipment_num"], "times": []}
#     for t_index, t in enumerate(e_u["times"]):
#         if t_index == 0:
#             new_val = math.ceil((products_1_count * t) / 60.0)
#         elif t_index == 1:
#             new_val = math.ceil((products_2_count * t) / 60.0)
#         else:
#             new_val = math.ceil((products_3_count * t) / 60.0)
#         str_u_e["times"].append(new_val)
#     table_2.append(str_u_e)
#
# table_3 = []
# for e_u in table_2:
#     str_u_e = {"equipment_num": e_u["equipment_num"], "equipment_count": 0}
#     equipment_count_value = sum(e_u["times"]) / (equ_year_h * load_coeff * time_coeff)
#     str_u_e["equipment_count"] = math.ceil(equipment_count_value)
#     table_3.append(str_u_e)
#
# table_4 = []
# for e_u in used_employees:
#     str_u_e = {"employee": e_u, "times": []}
#     # str_u_e["employee"]["title"] = employees[e_u["profession"]]["title"]
#     for r in manufactured_products:
#         product = get_product(r)
#         sum_value = 0
#         for op in product["operations"]:
#             if e_u["profession"] == get_equipment(product["operations"][op]["model"])["profession"] and e_u["rank"] == product["operations"][op]["rank"]:
#                 sum_value += product["operations"][op]["time"]
#         str_u_e["times"].append(sum_value)
#     table_4.append(str_u_e)
#
# table_5 = []
# for e_u in table_4:
#     str_u_e = {"employee": e_u["employee"], "times": []}
#     # str_u_e["employee"]["title"] = employees[e_u["employee"]["profession"]]["title_ru"]
#     for t_index, t in enumerate(e_u["times"]):
#         if t_index == 0:
#             new_val = math.ceil((products_1_count * t) / 60.0)
#         elif t_index == 1:
#             new_val = math.ceil((products_2_count * t) / 60.0)
#         else:
#             new_val = math.ceil((products_3_count * t) / 60.0)
#         str_u_e["times"].append(new_val)
#     table_5.append(str_u_e)
#
# table_6 = []
# for e_u in table_5:
#     str_u_e = {"employee": e_u["employee"], "employee_count": 0}
#     str_u_e["employee"]["title"] = employees[e_u["employee"]["profession"]]["title_ru"]
#     employee_count_value = sum(e_u["times"])
#     str_u_e["count"] = math.ceil(employee_count_value / (emp_year_h * time_coeff))
#     table_6.append(str_u_e)
