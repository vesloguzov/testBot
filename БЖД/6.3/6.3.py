# df = pd.read_excel('6.3.xlsx', sheet_name='Sheet1').T.to_dict().values()
import pandas as pd
import random
import math

variants = [{'substance': 'Кислота серная \(H_2SO_4\)', 'harmful_substance': 20000, 'maximum_concentration': 1.0,
             'room_volume': 20000},
            {'substance': 'Углерода оксид \(CO\)', 'harmful_substance': 470000, 'maximum_concentration': 20.0,
             'room_volume': 20000},
            {'substance': 'Аммиак \(NH_3\)', 'harmful_substance': 520000, 'maximum_concentration': 20.0,
             'room_volume': 20000},
            {'substance': 'Кислота муравьиная \(HCOOH\)', 'harmful_substance': 3000, 'maximum_concentration': 1.0,
             'room_volume': 2000},
            {'substance': 'Нитроформ \(CH(NO_2)_3\)', 'harmful_substance': 100, 'maximum_concentration': 0.5,
             'room_volume': 200},
            {'substance': 'Сероуглерод \(CS_2\)', 'harmful_substance': 5000, 'maximum_concentration': 1.0,
             'room_volume': 4000},
            {'substance': 'Метанол \(CH_3OH\)', 'harmful_substance': 10000, 'maximum_concentration': 5.0,
             'room_volume': 2000},
            {'substance': 'Марганец \(Mn\)', 'harmful_substance': 600, 'maximum_concentration': 0.2,
             'room_volume': 4000},
            {'substance': 'Кислота азотная \(HNO_3\)', 'harmful_substance': 5000, 'maximum_concentration': 2.0,
             'room_volume': 2000},
            {'substance': 'Нитробензол \(C_6H_5NO_2\)', 'harmful_substance': 7000, 'maximum_concentration': 3.0,
             'room_volume': 20000},
            {'substance': 'Анилин \(C_6H_5NH_2\)', 'harmful_substance': 200, 'maximum_concentration': 0.1,
             'room_volume': 2000},
            {'substance': 'Этанол \(C_2H_5OH\)', 'harmful_substance': 250000, 'maximum_concentration': 1000.0,
             'room_volume': 200},
            {'substance': 'Бензол \(C_6H_6\)', 'harmful_substance': 4000, 'maximum_concentration': 15.0,
             'room_volume': 200},
            {'substance': 'Фенол \(C_6H_5OH\)', 'harmful_substance': 500, 'maximum_concentration': 0.3,
             'room_volume': 2000},
            {'substance': 'Ацетон \((CH_3)_2CO\)', 'harmful_substance': 430000, 'maximum_concentration': 200.0,
             'room_volume': 2000},
            {'substance': 'Азота оксид (в пересчете на \(NO_2\))', 'harmful_substance': 8000, 'maximum_concentration': 5.0,
             'room_volume': 2000},
            {'substance': 'Ртуть металлическая \(Hg\)', 'harmful_substance': 100, 'maximum_concentration': 0.01,
             'room_volume': 10000},
            {'substance': 'Бенз(а)пирен \(C_{20}H_{12}\)', 'harmful_substance': 5, 'maximum_concentration': 0.00015,
             'room_volume': 20000},
            {'substance': 'Медь \(Cu\)', 'harmful_substance': 3000, 'maximum_concentration': 1.0,
             'room_volume': 2000},
            {'substance': 'Никель \(Ni\)', 'harmful_substance': 200, 'maximum_concentration': 0.05,
             'room_volume': 2000},
            {'substance': 'Ангидрид хромовый \(CrO_3\)', 'harmful_substance': 20, 'maximum_concentration': 0.01,
             'room_volume': 2000},
            {'substance': 'Сероводород \(H_2S\)', 'harmful_substance': 400, 'maximum_concentration': 10.0,
             'room_volume': 20},
            {'substance': 'Ангидрид серный \(SO_3\)', 'harmful_substance': 100, 'maximum_concentration': 1.0,
             'room_volume': 20},
            {'substance': 'Кислота серная \(H_2SO_4\)', 'harmful_substance': 500, 'maximum_concentration': 1.0,
             'room_volume': 200},
            {'substance': 'Электрокорунд \(Al_2O_3\)', 'harmful_substance': 250, 'maximum_concentration': 6.0,
             'room_volume': 20},
            {'substance': 'Углерода оксид \(CO\)', 'harmful_substance': 30000, 'maximum_concentration': 20.0,
             'room_volume': 1000},
            {'substance': 'Бутанол \(C_4H_9OH\)', 'harmful_substance': 20000, 'maximum_concentration': 10.0,
             'room_volume': 2000},
            {'substance': 'Ангидрид сернистый \(SO_2\)', 'harmful_substance': 350, 'maximum_concentration': 10.0,
             'room_volume': 20},
            {'substance': 'Аммиак \(NH_3\)', 'harmful_substance': 55000, 'maximum_concentration': 20.0,
             'room_volume': 2000},
            {'substance': 'Ацетон \((CH_3)_2CO\)', 'harmful_substance': 350000, 'maximum_concentration': 200.0,
             'room_volume': 2000}]

variant = variants[9]
substance = variant['substance']
harmful_substance = variant['harmful_substance']
maximum_concentration = variant['maximum_concentration']
room_volume = variant['room_volume']

L_pr = math.ceil(harmful_substance/(maximum_concentration - 0.3 * maximum_concentration))
K_r = math.ceil(L_pr/room_volume)

print(K_r)