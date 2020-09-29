import json

# открываем исходный файл
with open(file='../raw_files/litters.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)

# работа со столбцами...
for item in data:
    # удаление ненужных
    del item['pedigree_link']
    del item['image']
    del item['description']
    # замена названий столбцов на требуемые
    item['father'] = item.pop('f_id')
    item['mother'] = item.pop('m_id')
    item['breeder'] = item.pop('breeder_info')
    item['date_of_birth'] = item.pop('born_time')
    # замена строковых ID на числовые
    item['id'] = int(item['id'])
    item['father'] = int(item['father'])
    item['mother'] = int(item['mother'])
    # замена заводчика на его ID согласно persons_result.json
    if 'Жучкова И' in item['breeder']:
        item['breeder'] = 120
    elif 'Егоров А' in item['breeder']:
        item['breeder'] = 109
    elif 'Артарова В' in item['breeder']:
        item['breeder'] = 12
    # извлечение года рождения из поля name в отдельное поле
    item['year'] = item['name'][-4:]
    item['name'] = item['name'][:-5]
    # добавление ID префикса
    item['prefix'] = 1

    print(item)

# сохранить в json
with open('../result/litters_result.json', 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(data, ensure_ascii=False))
