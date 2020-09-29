import json

# открываем исходный файл
from shutil import copy

with open(file='../raw_files/rats.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)

# работа со столбцами...
for item in data:
    # удаление ненужных
    del item['f_info']
    del item['m_info']
    del item['grade']
    del item['image']
    del item['photo']
    del item['child_photo']
    del item['pedigree']
    del item['status']
    del item['health']
    del item['characteric']
    del item['exhibition']
    del item['autopsy_info']
    del item['bastards']
    # замена названий столбцов на требуемые
    item['information'] = item.pop('additional_info')
    item['variety'] = item.pop('type')
    item['father'] = item.pop('f_id')
    item['mother'] = item.pop('m_id')
    item['litter'] = item.pop('lit_id')
    item['date_of_birth'] = item.pop('born_time')
    item['date_of_death'] = item.pop('death_time')
    item['in_rattery'] = item.pop('in_nursery')
    item['breeder'] = item.pop('breeder_info')
    item['owner'] = item.pop('owner_info')
    # замена значений на требуемые
    if item['gender'] == 'm':
        item['gender'] = 'male'
    else:
        item['gender'] = 'female'
    if item['in_rattery'] == 'yes':
        item['in_rattery'] = True
    else:
        item['in_rattery'] = False
    # замена строковых ID на числовые
    item['id'] = int(item['id'])
    item['father'] = int(item['father'])
    item['mother'] = int(item['mother'])
    item['litter'] = int(item['litter'])
    # замена нулевого значения ID на None
    if item['litter'] == 0:
        item['litter'] = None
    if item['father'] == 0:
        item['father'] = None
    if item['mother'] == 0:
        item['mother'] = None
    if item['date_of_death'] == "0000-00-00":
        item['date_of_death'] = None

    # префикс "с Ромашкой" удаляется из имени и добавляется prefix_id = 1
    # префикс "без Ромашки" удаляется из имени и добавляется prefix_id = 2
    # префикс "Ratto Incanto" удаляется из имени и добавляется prefix_id = 3
    # префикс "из КДК СПб" удаляется из имени и добавляется prefix_id = 4
    # префикс "Rotte Verden" удаляется из имени и добавляется prefix_id = 5
    # префикс "с Планеты Крыс" удаляется из имени и добавляется prefix_id = 6
    # префикс "из Домика голубой Крысы" удаляется из имени и добавляется prefix_id = 7
    # префикс "из ДГК" удаляется из имени и добавляется prefix_id = 7
    # префикс "из Доброй Сказки" удаляется из имени и добавляется prefix_id = 8
    # префикс "из Вороньего гнезда" удаляется из имени и добавляется prefix_id = 9
    # префикс "Сибирский" удаляется из имени и добавляется prefix_id = 10
    # префикс "из Долины Нагваля" удаляется из имени и добавляется prefix_id = 11
    # префикс "Arctic Point" удаляется из имени и добавляется prefix_id = 12
    # префикс "Ashen Night" удаляется из имени и добавляется prefix_id = 13
    # префикс "Modus Vivendi" удаляется из имени и добавляется prefix_id = 14
    if 'с Ромашкой' in item['name'] or 'c Ромашкой' in item['name']:
        item['prefix'] = 1
        item['name'] = item['name'][:-11]
    elif 'без Ромашки' in item['name']:
        item['prefix'] = 2
        item['name'] = item['name'][:-12]
    elif 'Ratto Incanto' in item['name']:
        item['prefix'] = 3
        item['name'] = item['name'][14:]
    elif 'из КДК СПб' in item['name']:
        item['prefix'] = 4
        item['name'] = item['name'][:-11]
    elif 'Rotte Verden' in item['name']:
        item['prefix'] = 5
        item['name'] = item['name'][13:]
    elif 'с Планеты Крыс' in item['name']:
        item['prefix'] = 6
        item['name'] = item['name'][:-15]
    elif 'из Домика Голубой Крысы' in item['name']:
        item['prefix'] = 7
        item['name'] = item['name'][:-24]
    elif 'из ДГК' in item['name']:
        item['prefix'] = 7
        item['name'] = item['name'][:-7]
    elif 'из Доброй Сказки' in item['name']:
        item['prefix'] = 8
        item['name'] = item['name'][:-17]
    elif 'из Вороньего гнезда' in item['name']:
        item['prefix'] = 9
        item['name'] = item['name'][:-20]
    elif 'Сибирский' in item['name'] or 'Сибирская' in item['name']:
        item['prefix'] = 10
        item['name'] = item['name'][:-10]
    elif 'из Долины Нагваля' in item['name']:
        item['prefix'] = 11
        item['name'] = item['name'][:-18]
    elif 'Arctic Point' in item['name']:
        item['prefix'] = 12
        item['name'] = item['name'][13:]
    elif 'Ashen Night' in item['name']:
        item['prefix'] = 13
        item['name'] = item['name'][12:]
    elif 'Modus Vivendi' in item['name']:
        item['prefix'] = 14
        item['name'] = item['name'][14:]
    else:
        item['prefix'] = None

# открываем отредактированный файл со списком всех персон и заполняем список
with open(file='../txt/persons.txt', mode='r', encoding='utf-8') as f:
    persons = f.read().splitlines()

# приведение breeder_id и owner_id к индексу персоны в persons
for i in range(0, len(persons)):
    for d in data:
        if persons[i].split('.')[0] in d['breeder']:
            d['breeder'] = str(i)
        if persons[i].split('.')[0] in d['owner']:
            d['owner'] = str(i)

# None, если значение не совпало ни с одной фамилией из списка
for d in data:
    if len(d['breeder']) > 3:
        d['breeder'] = None
    if len(d['owner']) > 3:
        d['owner'] = None

    # замена строковых ID на числовые
    # if d['breeder_id'] is not None or '':
    #     d['breeder_id'] = int(d['breeder_id'])
    # if d['owner_id'] is not None or '':
    #     d['owner_id'] = int(d['owner_id'])

print(data)
print(len(data))

# # сохранить в json
# with open('result/rats_result.json', 'w', encoding='utf-8') as fh:
#     fh.write(json.dumps(data, ensure_ascii=False, indent=2))

for d in data:
    del d['litter']
    del d['father']
    del d['mother']

# сохранить в json без литер
with open('../result/rats_result_without_litters.json', 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(data, ensure_ascii=False, indent=2))
#
# for d in data:
#     del d['prefix']
#     del d['owner']
#     del d['breeder']
#     del d['in_rattery']
#     del d['date_of_death']
#     del d['date_of_birth']
#     del d['variety']
#     del d['information']
#     del d['gender']
#     del d['name']
#
# # сохранить в json ID, отцов, матерей и литеры
# with open('result/rats_litters.json', 'w', encoding='utf-8') as fh:
#     fh.write(json.dumps(data, ensure_ascii=False, indent=4))
