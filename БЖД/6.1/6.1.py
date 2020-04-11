import json
import random

source = [{'room': 'Офисное помещение', 'illumination_from': 200, 'illumination_to': 600,
           'illumination_system': 'при общем освещении', 'illumination_normal': 300},
          {'room': 'Операционный зал (кассовый зал, помещения пересчета денег)', 'illumination_from': 200,
           'illumination_to': 600, 'illumination_system': 'при общем освещении', 'illumination_normal': 400},
          {'room': 'Кабинеты и  комнаты преподавателей', 'illumination_from': 200, 'illumination_to': 600,
           'illumination_system': 'при общем освещении', 'illumination_normal': 300},
          {'room': 'Кабинеты врачей - педиатров', 'illumination_from': 200, 'illumination_to': 600,
           'illumination_system': 'при общем освещении', 'illumination_normal': 300},
          {'room': 'Торговые залы супермаркетов', 'illumination_from': 300, 'illumination_to': 500,
           'illumination_system': 'при общем освещении', 'illumination_normal': 500},
          {'room': 'Парикмахерские: мужской зал  ', 'illumination_from': 200, 'illumination_to': 500,
           'illumination_system': 'при общем освещении', 'illumination_normal': 400},
          {'room': 'Парикмахерские: косметический кабинет', 'illumination_from': 300, 'illumination_to': 700,
           'illumination_system': 'при комбинированном освещении (всего)', 'illumination_normal': 600},
          {'room': 'Студия звукозаписи: помещения для записи и прослушивания', 'illumination_from': 150,
           'illumination_to': 300, 'illumination_system': 'при общем освещении', 'illumination_normal': 200},
          {'room': 'Операционная', 'illumination_from': 400, 'illumination_to': 700,
           'illumination_system': 'при комбинированном освещении (всего)', 'illumination_normal': 500},
          {'room': 'Кассовые залы, билетные багажные кассы  на вокзале', 'illumination_from': 200,
           'illumination_to': 500, 'illumination_system': 'при общем освещении', 'illumination_normal': 300},
          {'room': 'Рецептурный отдел  в аптеке', 'illumination_from': 200, 'illumination_to': 500,
           'illumination_system': 'при общем освещении', 'illumination_normal': 300},
          {'room': 'Кабинеты массажа, лечебной физкультуры,', 'illumination_from': 150, 'illumination_to': 400,
           'illumination_system': 'при общем освещении', 'illumination_normal': 200},
          {'room': 'Кабинеты хирургов,  травматологов', 'illumination_from': 300, 'illumination_to': 700,
           'illumination_system': 'при общем освещении', 'illumination_normal': 500},
          {'room': 'Кабинеты дерматологов - аллергологов  ', 'illumination_from': 200, 'illumination_to': 500,
           'illumination_system': 'при общем освещении', 'illumination_normal': 500},
          {'room': 'Кабинеты стоматологов;', 'illumination_from': 200, 'illumination_to': 600,
           'illumination_system': 'при общем освещении', 'illumination_normal': 500},
          {'room': 'Ремонт часов, ювелирные и граверные работы;', 'illumination_from': 1000, 'illumination_to': 3000,
           'illumination_system': 'при комбинированном освещении (всего)', 'illumination_normal': 3000},
          {'room': 'Мастерские подгонки готового платья', 'illumination_from': 200, 'illumination_to': 500,
           'illumination_system': 'при общем освещении', 'illumination_normal': 400},
          {'room': 'Проектные залы и комнаты конструкторских бюро', 'illumination_from': 300, 'illumination_to': 700,
           'illumination_system': 'при комбинированном освещении (всего)', 'illumination_normal': 600},
          {'room': 'Помещения  тематических выставок', 'illumination_from': 150, 'illumination_to': 300,
           'illumination_system': 'при общем освещении', 'illumination_normal': 300},
          {'room': '  Залы ЭВМ', 'illumination_from': 200, 'illumination_to': 600,
           'illumination_system': 'при комбинированном освещении (всего)', 'illumination_normal': 500},
          {'room': 'Лаборатории органической и неорганической химии,', 'illumination_from': 200, 'illumination_to': 500,
           'illumination_system': 'при общем освещении', 'illumination_normal': 400},
          {'room': 'Горячие, холодные, заготовочные цеха в общепите', 'illumination_from': 200, 'illumination_to': 500,
           'illumination_system': 'при общем освещении', 'illumination_normal': 300},
          {'room': 'Торговый зал в магазине меховых изделий', 'illumination_from': 200, 'illumination_to': 500,
           'illumination_system': 'при общем освещении', 'illumination_normal': 300},
          {'room': 'Торговый зал в книжном магазине', 'illumination_from': 200, 'illumination_to': 500,
           'illumination_system': 'при общем освещении', 'illumination_normal': 300},
          {'room': 'Торговый зал в магазине стройматериалов', 'illumination_from': 200, 'illumination_to': 500,
           'illumination_system': 'при общем освещении', 'illumination_normal': 300},
          {'room': 'Рекламно - декорационные мастерские', 'illumination_from': 200, 'illumination_to': 500,
           'illumination_system': 'при комбинированном освещении (всего)', 'illumination_normal': 400},
          {'room': 'Ателье химчистки одежды: выведение пятен', 'illumination_from': 1000, 'illumination_to': 2500,
           'illumination_system': 'при комбинированном освещении (всего)', 'illumination_normal': 2000},
          {'room': 'Ателье пошива и ремонта одежды и трикотажных изделий: пошивочные цеха', 'illumination_from': 300,
           'illumination_to': 700, 'illumination_system': 'при общем освещении', 'illumination_normal': 750},
          {'room': 'Посты медсестер', 'illumination_from': 200, 'illumination_to': 500,
           'illumination_system': 'при общем освещении', 'illumination_normal': 300},
          {'room': 'Кабинет директора', 'illumination_from': 200, 'illumination_to': 600,
           'illumination_system': 'при общем освещении', 'illumination_normal': 300}]

good_class = False
bad_class_3_1 = False
bad_class_3_2 = False

variant = random.choice(source)
variant['illumination_current'] = random.randrange(variant['illumination_from'], variant['illumination_to'], 10)

variant_room = variant['room']
variant_system = variant['illumination_system']

E_n = variant['illumination_normal']
E_f = variant['illumination_current']
print(E_f, E_n)

if E_f >= E_n:
    good_class = True
elif E_f >= E_n * 0.5:
    bad_class_3_1 = True
else:
    bad_class_3_2 = True

print(good_class)
print(bad_class_3_1)
print(bad_class_3_2)